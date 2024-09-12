import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_candidate_info(text):
    """Extract candidate's information from the text."""
    # Define regex patterns for phone number, email, and name
    phone_pattern = r'\+?\d{9,}\d'
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    name_pattern = r'[A-Z][a-z]+(?: [A-Z][a-z]+)*'  # Very basic name pattern

    phone = re.search(phone_pattern, text)
    email = re.search(email_pattern, text)
    name = re.search(name_pattern, text)

    return {
        "first_name": name.group(0) if name else "Not Found",
        "email": email.group(0) if email else "Not Found",
        "mobile_number": phone.group(0) if phone else "Not Found",
    }
