FROM continuumio/miniconda3:latest

WORKDIR /app/app

COPY requirements.txt .

RUN grep -v "langchain" requirements.txt > requirements_modified.txt && \
    grep -v "langchain-community" requirements_modified.txt > requirements_final.txt

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

RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "rag-env", "/bin/bash", "-c"]

COPY . /app

RUN find /app -type d -exec touch {}/__init__.py \;


ENV PYTHONPATH=/app

EXPOSE 8000

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "rag-env"]


CMD ["python", "main.py"] 