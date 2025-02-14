# CV-to-Role Match Analyzer

## Project Overview

The core functionality of the CV-to_Role Match Analyzer revolves around comparing the skills and qualifications presented in a CV with the requirements outlined in a job description.  This comparison goes beyond simple keyword matching and aims to provide a more nuanced understanding of the candidate's fit.

The output JSON file includes the following key information:

*   **Numerical Match Score (0-100):** A quantitative measure representing the overall compatibility between the CV and the job description.  A higher score indicates a better match.
*   **Categorized Skill Gaps:** Identification of specific skills and qualifications mentioned in the job description that are missing or underrepresented in the CV. These gaps are categorized for clarity (Education, Work Experience, Skills, Certifications).
*   **Specific Improvement Recommendations:**  Actionable suggestions for the candidate to improve their CV and better align it with the target role.  These recommendations might include highlighting relevant projects, acquiring new skills, or rephrasing existing experience.

### Key Features

*   **Automated Analysis:**  Eliminates the need for manual CV screening, saving recruiters valuable time.
*   **Objective Evaluation:**  Provides a data-driven approach to candidate assessment, reducing bias and promoting fairness.
*   **Detailed Insights:**  Offers granular information about skill gaps and areas for improvement, facilitating more targeted feedback.
*   **JSON Output:**  Enables easy integration with other recruitment systems and tools.
*   **PDF Input:** Accepts CVs and Job Descriptions in the commonly used PDF format.

### Target Audience

This tool is beneficial for:

*   **Recruiters:**  Quickly identify qualified candidates and prioritize their applications.
*   **Hiring Managers:**  Gain a deeper understanding of candidate strengths and weaknesses.
*   **Job Seekers:**  Identify areas where their CV can be improved to better match target roles.

### Technical Stack

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

## Project Phases

### Phase 1: Requirements Engineering

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

### Phase 2: Architecture
- **Command-line Interface Specification:** (Inline description of CLI arguments)
- **File System Interactions:** (Inline explanation of input/output files)
- **Third-party Libraries:** (Inline list of libraries used)
- **Team Member Responsibilities:** (Inline description of roles)
- [LLM Interaction Documentation](link-to-llm-docs)

### Phase 3: Design
- **Simple Design Principles (XP):** (Inline summary of how XP principles were followed)
- **CRC Description of Key Classes:** (Inline brief description of key classes and their responsibilities)
- [LLM Interaction Documentation](link-to-llm-docs)

### Phase 4: Coding & Testing

#### Coding
- **Code Quality:** Adherence to clean coding practices and PEP 8.
- **Project File Structure:**
  
| File Name | Description |
|-----------|-------------|
| `main.py` | Entry point for the project |
| `utils.py` | Utility functions |
| `config.json` | Configuration settings |

#### Testing
- **Automated Unit Test:** (Inline description & link to test file)
- **System-level Functional Test:** (Inline description & link to test file)
- [LLM Interaction Documentation](link-to-llm-docs)

### Phase 5: Documentation
- README should be concise, clear, and well-formatted.
- Ensure smooth user experience by maintaining accurate information.

