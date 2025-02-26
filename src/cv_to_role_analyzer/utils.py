import pypdf


class RoleProcessor:
    @staticmethod
    def process(role_path):
        """Reads job role description from a text file."""
        with open(role_path, "r", encoding="utf-8") as file:
            return file.read().strip()


class PDFProcessor:
    @staticmethod
    def extract_text(pdf_path):
        """Extracts text from a given PDF file."""
        with open(pdf_path, "rb") as file:
            reader = pypdf.PdfReader(file)
            return " ".join(page.extract_text() for page in reader.pages if page.extract_text())
