from setuptools import setup, find_packages

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Kannan M",
    author_email="kannandeveloper1771@gmail.com",
    description="A Python package for generating multiple-choice questions using LLMs and LangChain.",
    install_requires=[
        "openai",
        "langchain",
        "streamlit",
        "python-dotenv",
        "PyPDF2",
        "transformers",
        "torch",
        "huggingface_hub",
        "accelerate",
        "sentencepiece",
        "bitsandbytes"
    ],
    packages=find_packages(),

)