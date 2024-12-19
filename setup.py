from setuptools import find_packages, setup

def get_packages(path):
    with open(path, 'r') as f:
        requirements =  [line.strip() for line in f.readlines() if line.strip()] 

        if "-e ." in requirements:
            requirements.remove("-e .")
    
    return requirements

setup(
    name="PhonePricePrediction",
    version="0.0.1",
    author="Anshuman jain",
    author_email="anshumanjain8886@gmail.com",
    packages=find_packages(),
    install_requires=get_packages("requirements.txt"),
    description="A Machine Learning model to predict the price of a phone based on its specifications",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/anshumanjain8886/PhonePricePrediction",
)