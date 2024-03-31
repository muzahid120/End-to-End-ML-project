from setuptools import find_packages, setup
from typing import List

hypen_dot = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return a list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements] 
        if hypen_dot in requirements:
            requirements.remove(hypen_dot)

    return requirements

setup(
    name='ML Project',
    version='0.0.1',
    author='Sk Muzahid',
    author_email='muzahidsk771@gmail.com',  # Fixed email format
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
