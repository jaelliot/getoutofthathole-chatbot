import mmh3

HASH_FILE = "chroma/data_hash.txt"

def calculate_file_hash(file_path):
    """Calculate the hash of a file using MurmurHash."""
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return mmh3.hash_bytes(data).hex()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def calculate_documents_hash(documents):
    """Calculate the hash of documents using MurmurHash."""
    combined_data = "".join(doc.page_content for doc in documents)
    return mmh3.hash_bytes(combined_data.encode('utf-8')).hex()

def has_content_changed(documents):
    """Check if the content has changed."""
    current_hash = calculate_documents_hash(documents)

    try:
        with open(HASH_FILE, "r") as f:
            saved_hash = f.read().strip()
    except FileNotFoundError:
        saved_hash = ""

    if saved_hash == current_hash:
        return False

    with open(HASH_FILE, "w") as f:
        f.write(current_hash)
    return True
