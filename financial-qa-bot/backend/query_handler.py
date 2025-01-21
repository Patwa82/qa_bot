import numpy as np

def process_query(query, extracted_data, embeddings):
    """
    Processes a query and retrieves relevant data and an answer.
    Args:
        query (str): User's financial query.
        extracted_data (DataFrame): Parsed financial data.
        embeddings (dict): Precomputed embeddings for document retrieval.
    Returns:
        str: Generated answer.
        DataFrame: Relevant data from the P&L table.
    """
    # Placeholder: You'd typically use a model like T5 or GPT here
    # For now, we simulate an answer and find relevant rows
    relevant_rows = extracted_data[
        extracted_data.apply(lambda row: query.lower() in row.to_string().lower(), axis=1)
    ]
    
    if not relevant_rows.empty:
        answer = f"Based on your query, here's what we found: {query}"
    else:
        answer = "No relevant data found for your query."
    
    return answer, relevant_rows
