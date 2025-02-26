import os


class AnalysisRequest:
    @staticmethod
    def validate(cv, role_text):
        """Validates input parameters."""
        if not os.path.exists(cv):
            raise FileNotFoundError(f"The CV file {cv} does not exist.")
        if not os.path.exists(role_text):
            raise FileNotFoundError(f"The job description {role_text} does not exist.")

    @staticmethod
    def process(cv, role_text):
        """Validates inputs and processes data."""
        AnalysisRequest.validate(cv, role_text)
        return {"cv": cv, "role_text": role_text}
