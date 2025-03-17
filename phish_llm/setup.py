from setuptools import setup, find_packages

setup(
    name="phish_llm",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv",
        "openai",
    ],
    python_requires=">=3.8",
)