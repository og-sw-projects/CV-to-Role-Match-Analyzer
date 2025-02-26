import json


class AnalysisReport:
    def __init__(self, analysis_data):
        self.match_score = analysis_data.get("match_score", 0)
        self.skill_gaps = analysis_data.get("skill_gaps", [])
        self.recommendations = analysis_data.get("recommendations", [])

    def to_json(self):
        """Converts analysis results into JSON format."""
        return json.dumps({
            "match_score": self.match_score,
            "skill_gaps": self.skill_gaps,
            "recommendations": self.recommendations
        }, indent=4)
