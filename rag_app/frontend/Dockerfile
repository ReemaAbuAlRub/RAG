# rag_app/frontend/Dockerfile

# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the frontend code into the container
COPY . .

# Expose port 8501 (default for Streamlit)
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "streamlit_app.py", "--server.port", "8501", "--server.enableCORS", "false"]
