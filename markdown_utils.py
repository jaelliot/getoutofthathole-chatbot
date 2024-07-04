import re

def strip_markdown(text):
    # Remove Markdown links
    text = re.sub(r'\[([^\[]+)\]\([^\)]+\)', r'\1', text)
    # Remove inline code
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # Remove bold and italic formatting
    text = re.sub(r'(\*\*|__)(.*?)\1', r'\2', text)
    text = re.sub(r'(\*|_)(.*?)\1', r'\2', text)
    # Replace multiple newlines with a single newline
    text = re.sub(r'\n\s*\n', '\n', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Ensure newlines after punctuation
    text = re.sub(r'(\.|\!|\?)\s*', r'\1\n', text)
    # Ensure proper formatting for lists and paragraphs
    text = re.sub(r'(\d+\.\s)', r'\n\1', text)
    text = re.sub(r'(\-|\*)\s', r'\n- ', text)
    text = re.sub(r'\n+', '\n', text)
    return text.strip()
