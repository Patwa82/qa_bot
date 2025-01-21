import pickle

def load_embeddings(file_path="../embeddings/embeddings.pkl"):
    """
    Loads precomputed embeddings from a file.
    Args:
        file_path (str): Path to the embeddings file.
    Returns:
        dict: Loaded embeddings.
    """
    try:
        with open(file_path, "rb") as f:
            embeddings = pickle.load(f)
        return embeddings
    except FileNotFoundError:
        raise FileNotFoundError("Embeddings file not found. Please ensure embeddings are generated.")
