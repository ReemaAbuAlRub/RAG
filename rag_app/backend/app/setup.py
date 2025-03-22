from setuptools import find_packages,setup

setup(
    name='Rag Application',
    version='0.0.1',
    author= 'Reema Maen',
    install_requires=[
        "fastapi>=0.70.0",
        "uvicorn>=0.15.0",
        "faiss-cpu>=1.7.2", 
        "sentence-transformers>=2.2.2",
        "transformers>=4.29.2",
        "PyPDF2>=1.26.0",
        'openai'
    ],
    packages=find_packages()
)