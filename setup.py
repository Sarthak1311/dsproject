from setuptools import find_packages, setup
from typing import List


Hypen_dot_e = '-e .'


def get_req(file_path:str)->List:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements =[req.replace('\n','') for req in requirements]
        if Hypen_dot_e in requirements:
            requirements.remove(Hypen_dot_e)
    return requirements






setup(
    name = "MLProject",
    version= '0.0.1',
    author="Sarthak tyagi",
    author_email="samtyagi1311@gmail.com",
    packages=find_packages(),
    install_requires=get_req("requirements.txt")
)