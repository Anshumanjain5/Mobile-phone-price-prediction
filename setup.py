from setuptools import find_packages, setup
import os

def get_packages(path):
    """
    Reads a requirements file and returns a list of dependencies.

    Args:
        path (str): The file path to the requirements file.

    Returns:
        list: A list of required dependencies.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"The specified requirements file '{path}' does not exist.")
    
    with open(path, 'r') as f:
        requirements = [line.strip() for line in f.readlines() if line.strip()]

        # Remove editable package reference if present
        if "-e ." in requirements:
            requirements.remove("-e .")
    
    return requirements

setup(
    name="PhonePricePrediction",
    version="0.0.1",
    author="Anshuman Jain",
    author_email="anshumanjain8886@gmail.com",
    packages=find_packages(),
    install_requires=get_packages("requirements.txt"),
    description="A Machine Learning model to predict the price of a phone based on its specifications",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/anshumanjain8886/PhonePricePrediction",
    python_requires='>=3.6',  # Specify the minimum required Python version
)
