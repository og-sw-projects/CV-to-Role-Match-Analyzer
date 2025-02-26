import json
import os
import re

from dotenv import load_dotenv
from google.genai import Client, errors
from google.genai.types import Content, Part

# todo: add documentation to all classes
# todo: update prompt to give more than just a few


class LLMClient:
    @staticmethod
    def analyze_match(cv_text, role_text):
        """Generates an optimized prompt and calls Gemini API."""

        prompt = LLMClient._generate_prompt(cv_text, role_text)
        response = LLMClient._call_llm_api(prompt)

        # If response lacks required fields, retry with a refined prompt
        if not response or "match_score" not in response:
            response = LLMClient._call_llm_api(LLMClient._refine_prompt(prompt, response))

        return response

    @staticmethod
    def _generate_prompt(cv_text, role_text):
        """Creates an optimized LLM prompt using few-shot learning & CoT reasoning."""

        prompt = Content(parts=[
            # Role
            Part(text="You are an advanced AI specializing in CV analysis."),
            # Instructions
            Part(text=f"Evaluate the candidate’s CV against the job description and provide the results in JSON format"
                      f"with the following keys:\n"
                      "- `match_score` (integer, 0-100)\n"
                      "- `skill_gaps` (list of dictionaries, each with 'category' and 'gap' keys)\n"
                      "- `recommendations` (list of strings)\n\n"
                      "Use structured reasoning before generating the JSON. Ensure the JSON is valid and parsable."),
            # CV Text
            Part(text=f"CV Text:\n{cv_text}"),
            # Role Description
            Part(text=f"Role Description:\n{role_text}"),
        ])

        return prompt

    @staticmethod
    def _call_llm_api(prompt):
        """Calls the Gemini API with the given prompt, parses the JSON response, and returns it as a dictionary"""

        try:
            # Load environment variables from .env file and get API key from environment
            load_dotenv()
            api_key = os.getenv("API_KEY")
            if not api_key:
                raise ValueError("API_KEY environment variable not set.")

            # Initialize Gemini client and generate content
            client = Client(api_key=api_key)
            response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)

            # Extract response test, find JSON object, parse and return
            response_text = response.candidates[0].content.parts[0].text
            match = re.search(r"{.*}", response_text, re.DOTALL)
            return json.loads(match.group(0))

        except (
            errors.ClientError,
            errors.APIError,
            errors.FunctionInvocationError,
            errors.ExperimentalWarning,
            errors.UnknownFunctionCallArgumentError,
            errors.UnsupportedFunctionError,
        ) as e:
            print(f"GenAI Error: {type(e).__name__}: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except Exception as e:  # Catch other potential errors (e.g., network issues)
            print(f"An unexpected error occurred: {e}")
            return None

    @staticmethod
    def _refine_prompt(prompt, response):
        """Refines prompt if the initial LLM response is incomplete."""

        prompt.parts.append(Part(text="\nEnsure all required fields are included."))
        prompt.parts.append(Part(text=f"\nPrevious response: {response}"))
        return prompt
