# CV-to-Role Match Analyzer

## Project Overview

The core functionality of the CV-to-Role Match Analyzer revolves around comparing the skills and qualifications presented in a CV with the requirements outlined in a job description.  This comparison goes beyond simple keyword matching and aims to provide a more nuanced understanding of the candidate's fit.

The output JSON file includes the following key information:

*   **Numerical Match Score (0-100):** A quantitative measure representing the overall compatibility between the CV and the job description.  A higher score indicates a better match.
*   **Categorized Skill Gaps:** Identification of specific skills and qualifications mentioned in the job description that are missing or underrepresented in the CV. These gaps are categorized for clarity (Education, Work Experience, Skills, Certifications).
*   **Specific Improvement Recommendations:**  Actionable suggestions for the candidate to improve their CV and better align it with the target role.  These recommendations might include highlighting relevant projects, acquiring new skills, or rephrasing existing experience.

#### Key Features

*   **Automated Analysis:**  Eliminates the need for manual CV screening, saving recruiters valuable time.
*   **Objective Evaluation:**  Provides a data-driven approach to candidate assessment, reducing bias and promoting fairness.
*   **Detailed Insights:**  Offers granular information about skill gaps and areas for improvement, facilitating more targeted feedback.
*   **JSON Output:**  Enables easy integration with other recruitment systems and tools.
*   **PDF Input:** Accepts CVs and Job Descriptions in the commonly used PDF format.

#### Target Audience

This tool is beneficial for:

*   **Recruiters:**  Quickly identify qualified candidates and prioritize their applications.
*   **Hiring Managers:**  Gain a deeper understanding of candidate strengths and weaknesses.
*   **Job Seekers:**  Identify areas where their CV can be improved to better match target roles.

#### Technical Stack

*   Programming Language: Python
*   Libraries/Frameworks: PyPDF2, Pandas

## Installation Guide

Step-by-step instructions to install dependencies and set up the project. TODO

```bash
# Example installation steps TODO
git clone <repository-url>
cd <project-directory>
pip install -r requirements.txt
```

Ensure the guide is clear and glitch-free. TODO

## Usage Examples

Provide usage instructions with examples, including sample inputs and expected outputs. TODO

```bash
# Example command to run the project TODO
python main.py --input sample.pdf --output results.json
```

## Requirements Engineering

#### Functional Feature Requirements:
- **Input Processing (Functional Suitability - Functional Completeness)**
  - FR1.1: The system shall accept PDF format CVs as input files up to 10MB in size.
  - FR1.2: The system shall accept role descriptions as text input up to 2000 characters.
  - FR1.3: The system shall successfully extract text from PDF CVs with 100% text content preservation.
- **Analysis Processing (Functional Suitability - Functional Appropriateness)**
  - FR2.1: The system shall extract and categorize CV components into:
    - Education (degrees, institutions, dates).
    - Work experience (roles, companies, dates, responsibilities).
    - Skills (technical, soft skills).
    - Certifications.
  - FR2.2: The system shall identify from role descriptions:
    - Required education.
    - Required experience level.
    - Required skills (minimum 80% accuracy).
    - Required certifications.
- **Matching Analysis (Functional Suitability - Functional Correctness)**
  - FR3.1: The system shall generate a numerical match score (0-100).
  - FR3.2: The system shall identify all skill gaps and categorize them as:
    - Critical (required but missing).
    - Important (preferred but missing).
    - Nice-to-have (mentioned but missing).
- **Output Generation (Functional Suitability - Functional Completeness)**
  - FR4.1: The system shall generate a JSON report containing:
    - Overall match score.
    - Categorized skill gaps.
    - Specific improvement recommendations.
#### Non-Functional Feature Requirements:
- **Performance Efficiency (Time Behavior)**
  - NFR1.1: The system shall complete analysis within 30 seconds.
- **Reliability (Maturity)**
  - NFR2.1: The system shall maintain 95% accuracy in requirement identification.
- **Security (Confidentiality)**
  - NFR3.1: The system shall not persist any CV data beyond the analysis session.
#### Acceptance Criteria:
- **PDF Processing**
  - AC1: Complete text extraction with preserved formatting for PDFs of sizes 1KB to 10MB.
- **Match Score Accuracy**
  - AC2: Consistent scoring (±5% variance for same inputs).
- **Skill Gap Identification**
  - AC3: 90% accuracy in identifying critical gaps.
#### [LLM Interaction Documentation](./chats/requirements_engineering_LLM_interactions.txt)

## Architecture
#### Command-line Interface Specification
```bash
# Main analysis command
cvanalyzer analyze --cv <path_to_pdf> --role <path_to_txt>

# Optional parameters
cvanalyzer analyze --cv <path_to_pdf> --role <path_to_txt> --output-dir <path>
cvanalyzer analyze --cv <path_to_pdf> --role <path_to_txt> --verbose [0|1|2]

# Utility commands
cvanalyzer --help
cvanalyzer --version
```
#### File System Interactions
The system interacts with files in the following manner:
- Input Files:
  - CV: PDF format.
  - Role Description: Text file.
- Output Files:
  - Analysis Report: JSON format containing match score, skill gaps, and recommendations. Output directory can be specified via command line. If not specified, a default output location will be used.
- Temporary Files:
  - The system utilizes temporary files during analysis. These files are automatically managed and cleaned up by the system.

#### Third-Party Libraries
The system leverages third-party libraries for specific functionalities:
- PDF processing and text extraction.
- Data structuring and analysis.
- Large Language Model (LLM) API integration.
- Command-line interface management.
- Data validation.

#### Team Member Responsibilities
The project is divided into two main areas of responsibility:
- Data Handling and Interface: This area encompasses managing input data (CV and role description), interacting with the file system, and providing the command-line interface.
- Analysis and LLM Integration: This area focuses on integrating with the LLM API, developing the analysis algorithms, and generating the final report.

Both team members share responsibility for code review, documentation, integration testing, and performance optimization.
#### [LLM Interaction Documentation](./chats/architecture_LLM_chats.txt)

## Design
#### CRC Description of Key Classes:
- **CVAnalyzer**
  - *Responsibilities*
    - Coordinates the overall analysis process
    - Extracts text from CV PDFs
    - Processes role descriptions
    - Generates match analysis reports
    - Manages LLM interactions for analysis
  - *Collaborators*
    - AnalysisReport
    - SkillGap
    - LLM Client (external)
    - PDF Processor (external)
- **AnalysisReport**
  - *Responsibilities*
    - Holds analysis results (match score, gaps, recommendations)
    - Converts analysis data to JSON format
    - Validates score ranges (0-100)
    - Maintains structured representation of analysis results
  - *Collaborators*
    - SkillGap
    - JSON library (external)
- **SkillGap**
  - *Responsibilities*
    - Represents a single identified skill gap
    - Stores gap category and description
    - Associates gap with importance level (critical/important/nice-to-have)
  - *Collaborators*
    - SkillGapType
- **SkillGapType**
  - *Responsibilities*
    - Defines valid gap importance levels
    - Ensures type safety for gap classifications
    - Provides string representation of gap types
  - *Collaborators*
    - None (Pure enumeration)
#### [LLM Interaction Documentation](./chats/design_LLM_interactions.txt)

## Coding & Testing

### Coding
- **Code Quality:** Adherence to clean coding practices and PEP 8.
- **Project File Structure:**
  
| File Name | Description |
|-----------|-------------|
| `main.py` | Entry point for the project |
| `utils.py` | Utility functions |
| `config.json` | Configuration settings |

### Testing
- **Automated Unit Test:** (Inline description & link to test file)
- **System-level Functional Test:** (Inline description & link to test file)
- [LLM Interaction Documentation](link-to-llm-docs)

