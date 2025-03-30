# Use Conda official image
FROM continuumio/miniconda3:latest

# Set working directory
WORKDIR /app/app

# Copy requirements.txt
COPY requirements.txt .

# Create a modified requirements file with compatible versions
RUN grep -v "langchain" requirements.txt > requirements_modified.txt && \
    grep -v "langchain-community" requirements_modified.txt > requirements_final.txt

# Create a environment.yml file with compatible package versions
# In your Dockerfile where you create the environment.yml file
RUN echo "name: rag-env" > environment.yml && \
    echo "channels:" >> environment.yml && \
    echo "  - conda-forge" >> environment.yml && \
    echo "  - defaults" >> environment.yml && \
    echo "dependencies:" >> environment.yml && \
    echo "  - python=3.9" >> environment.yml && \
    echo "  - pip" >> environment.yml && \
    echo "  - faiss-cpu" >> environment.yml && \
    echo "  - pip:" >> environment.yml && \
    echo "    - -r requirements_final.txt" >> environment.yml && \
    echo "    - langchain==0.3.21" >> environment.yml && \
    echo "    - langchain-community==0.3.20" >> environment.yml && \
    echo "    - langchain-openai" >> environment.yml && \
    echo "    - python-dotenv" >> environment.yml && \
    echo "    - python-multipart" >> environment.yml

# Create the Conda environment
RUN conda env create -f environment.yml

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "rag-env", "/bin/bash", "-c"]

# Copy the project code
COPY . /app

# Create __init__.py files to make directories into packages
RUN find /app -type d -exec touch {}/__init__.py \;

# Set PYTHONPATH to include the app directory
ENV PYTHONPATH=/app

# Expose the port for the API
EXPOSE 8000

# Set up the entrypoint
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "rag-env"]

# Run the application
CMD ["python", "main.py"] 