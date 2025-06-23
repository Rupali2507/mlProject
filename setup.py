from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."
def getRequirements(file_path)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path, "r") as f:
        requirements= f.readlines()
        [req.replace("\n","") for  req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="mlProject",
    version="0.0.1",
    author="Rupali",
    author_email="rupalik.ug23.ma@nitp.ac.in",
    packages=find_packages(),
    install_requires=getRequirements("requirements.txt"),
    description="A small ML project",
)