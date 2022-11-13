from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="python-pacotes-processamento-imagens",
    version="0.0.1",
    author="Layanne",
    author_email="Layannepereiraa28@gmail.com",
    description="Test version - Image processing. This package is a demo for simulation of upload on the Test Pypi website, and it's from class of the Bootcamp Unimed-BH Data Science is for professionals who already work with data science or are starting.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LayannePereira/Py_pacotes_processamento_imagens",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)