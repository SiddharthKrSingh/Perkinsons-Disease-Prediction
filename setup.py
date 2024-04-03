from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT="-e."

def get_items(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="Perkinsons Disease Prediction",
    version= "0.0.1",
    author_name="Siddharth Kumar Singh",
    author_email="siddharthsingh590@gmail.com",
    packages= find_packages(),
    required_items=get_items("requirements.txt")

)