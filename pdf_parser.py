from pypdf import PdfReader

def extract_text_from_pdf(uploaded_file):
    """
    Extract text from uploaded PDF.
    """

    try:
        reader = PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        if text.strip() == "":
            return "ERROR: No text found in PDF."

        return text

    except Exception as e:
        return f"ERROR: {str(e)}"