import click
import os

from src.cv_to_role_analyzer.llm import LLMClient
from src.cv_to_role_analyzer.report import AnalysisReport
from src.cv_to_role_analyzer.utils import PDFProcessor, RoleProcessor


def analyze_core(cv_text, role_text):  # Internal function, no click decorators
    """Analyzes a CV against a job description (core logic)."""
    analysis = LLMClient.analyze_match(cv_text, role_text)
    return AnalysisReport(analysis).to_json()  # Return JSON string


@click.command()
@click.option("--cv", required=True, help="Path to the CV PDF file.")
@click.option("--role", required=True, help="Path to the job role text file.")
@click.option("--output-dir", help="Path to the output directory (optional).")
@click.option("--verbose", type=click.IntRange(0, 2), default=1,
              help="Verbosity level (0: silent, 1: summary, 2: full JSON).")
@click.version_option("1.0")
def analyze_cli(cv, role, output_dir, verbose):  # Click wrapper function
    """CV Analyzer: Analyzes CVs against job roles (CLI entry point)."""
    try:
        role_text = RoleProcessor.process(role)
        cv_text = PDFProcessor.extract_text(cv)
        json_report = analyze_core(cv_text, role_text)  # Call core logic
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, "analysis_result.json")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(json_report)
            click.echo(f"Analysis saved to {output_path}")

        if verbose > 0:
            click.echo(json_report if verbose == 2 else "Analysis completed successfully!")

    except Exception as e:
        click.echo(f"An error occurred: {e}", err=True)
        click.echo("Analysis failed.", err=True)
        return 1  # Return an error code (non-zero)


if __name__ == "__main__":
    analyze_cli()
