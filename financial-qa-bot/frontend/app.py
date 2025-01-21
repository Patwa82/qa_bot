import streamlit as st
import os
from backend.document_parser import parse_pdf
from backend.query_handler import process_query
from backend.embeddings import load_embeddings

# Page title
st.title("Financial QA Bot")
st.write("Upload a PDF with P&L tables and ask questions about the data!")

# Sidebar for file upload
uploaded_file = st.sidebar.file_uploader("Upload a PDF", type=["pdf"])

# Load embeddings and models
st.sidebar.write("Loading models and embeddings...")
embeddings = load_embeddings()

# Default file path for testing
default_file_path = os.path.join("..", "data", "D:\financial qa bot\financial-qa-bot\data\Sample Financial Statement.pdf")

if uploaded_file:
    # Use the uploaded file
    st.sidebar.write("Processing the uploaded document...")
    extracted_data = parse_pdf(uploaded_file)
elif os.path.exists(default_file_path):
    # Use the default file for testing if no file is uploaded
    st.sidebar.write(f"Using default PDF: {default_file_path}")
    with open(default_file_path, "rb") as default_file:
        extracted_data = parse_pdf(default_file)
else:
    extracted_data = None
    st.write("Please upload a PDF to get started or ensure the default file exists in the 'data/' directory.")

# Display extracted data and allow queries
if extracted_data is not None:
    # Display extracted data
    st.write("### Extracted Financial Data")
    st.dataframe(extracted_data)

    # Input query
    query = st.text_input("Ask a question about the data:")

    if query:
        # Process the query
        st.write("### Answer")
        answer, relevant_data = process_query(query, extracted_data, embeddings)

        # Display answer and relevant data
        st.write(answer)
        st.write("### Relevant Data from the P&L Table")
        st.dataframe(relevant_data)
