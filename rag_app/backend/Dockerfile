 # rag_app/backend/Dockerfile

# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the backend code into the container
COPY . .

# Expose port 8000 (default for FastAPI)
EXPOSE 8000

# Command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
