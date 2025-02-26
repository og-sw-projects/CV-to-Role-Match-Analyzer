import json
import pytest
from src.cv_to_role_analyzer.cv_analyzer import analyze_core


def test_system_analyze_core(mocker, tmp_path):
    mock_response = {
        "match_score": 85,
        "skill_gaps": [{"category": "Tech", "gap": "Java"}],
        "recommendations": ["Learn Java"]
    }
    mocker.patch("src.cv_to_role_analyzer.llm.LLMClient.analyze_match", return_value=mock_response)

    cv_file_path = "tests/data/test_cv.txt"
    role_file_path = "tests/data/test_role.txt"

    with open(cv_file_path, "r") as f:
        cv_text = f.read()
    with open(role_file_path, "r") as f:
        role_text = f.read()

    report_json = analyze_core(cv_text, role_text)  # Call analyze_core directly
    report = json.loads(report_json)

    assert report == mock_response

    # Test with different input files
    test_cv2_path = tmp_path / "test_cv2.txt"
    test_role2_path = tmp_path / "test_role2.txt"

    with open(test_cv2_path, "w") as f:
        f.write("test cv 2")
    with open(test_role2_path, "w") as f:
        f.write("test role 2")

    with open(test_cv2_path, "r") as f:
        cv_text2 = f.read()
    with open(test_role2_path, "r") as f:
        role_text2 = f.read()

    report_json2 = analyze_core(cv_text2, role_text2)
    report2 = json.loads(report_json2)

    # Test with exception in LLMClient.analyze_match
    mocker.patch("src.cv_to_role_analyzer.llm.LLMClient.analyze_match", side_effect=Exception("LLM Error"))

    with pytest.raises(Exception, match="LLM Error"):
        analyze_core(cv_text, role_text)
