# Use the official Python 3.10 image from Docker Hub
FROM python:3.10.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY app/ ./app/

# Set PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Expose the default HTTP port
EXPOSE 80

# Command to run the Streamlit app
CMD ["streamlit", "run", "app/chatbot.py", "--server.port=80", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]
