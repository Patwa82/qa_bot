import pdfplumber
import pandas as pd

def parse_pdf(file):
    """
    Extracts tables from a PDF file and returns them as a structured DataFrame.
    Args:
        file: The uploaded PDF file.
    Returns:
        DataFrame: Extracted financial data from the PDF.
    """
    tables = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            # Extract tables from each page
            page_tables = page.extract_tables()
            for table in page_tables:
                tables.append(pd.DataFrame(table[1:], columns=table[0]))
    
    # Combine all tables into a single DataFrame
    if tables:
        return pd.concat(tables, ignore_index=True)
    else:
        raise ValueError("No tables found in the uploaded PDF.")
