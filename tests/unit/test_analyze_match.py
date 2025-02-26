import pytest
import json
from src.cv_to_role_analyzer.cv_analyzer import analyze_core


@pytest.mark.parametrize(
    "mock_response, cv_text, role_text, raises_exception, exception_message",
    [
        (  # Test case 1: Successful match
            {"match_score": 85, "skill_gaps": [{"category": "Tech", "gap": "Java"}], "recommendations": ["Learn Java"]},
            "Mock CV Text",
            "Mock Role Text",
            False,  # Does not raise an exception
            None,
        ),
        (  # Test case 2: Different match
            {"match_score": 92, "skill_gaps": [], "recommendations": ["Improve communication"]},
            "Mock CV Text",
            "Mock Role Text",
            False,
            None,
        ),
        (  # Test case 3: Empty CV
            {"match_score": 0, "skill_gaps": [], "recommendations": ["Provide a CV"]},
            "",
            "Mock Role Text",
            False,
            None,
        ),
        (  # Test case 4: Empty Role
            {"match_score": 0, "skill_gaps": [], "recommendations": ["Provide a job description"]},
            "Mock CV Text",
            "",
            False,
            None,
        ),
        (  # Test case 5: Special characters in CV
            {"match_score": 70, "skill_gaps": [], "recommendations": ["Review CV for special characters"]},
            "Mock CV Text with !@#$%^&*()",
            "Mock Role Text",
            False,
            None,
        ),
        (  # Test case 6: LLM error (exception case)
            None,  # No mock response for exception
            "Mock CV Text",
            "Mock Role Text",
            True,  # Raises an exception
            "LLM Error", # Exception message
        ),
        # Add more test cases as needed
    ],
)
def test_analyze_core(mocker, mock_response, cv_text, role_text, raises_exception, exception_message):
    if raises_exception:
        mocker.patch("src.cv_to_role_analyzer.llm.LLMClient.analyze_match", side_effect=Exception(exception_message))
        with pytest.raises(Exception, match=exception_message):
            analyze_core(cv_text, role_text)
    else:
        mocker.patch("src.cv_to_role_analyzer.llm.LLMClient.analyze_match", return_value=mock_response)
        report_json = analyze_core(cv_text, role_text)
        report = json.loads(report_json)
        assert report == mock_response
