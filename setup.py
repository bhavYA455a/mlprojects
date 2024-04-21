from setuptools import find_packages,setup
from typing import List
hyper ='-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    this func will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        ##readlines read a single line at a time so \n while create problem in it for that is used in place to it 
        requirements=[req.replace("\n","")for req in requirements]
        
        if hyper in requirements:
            requirements.remove(hyper)
    return requirements        
setup(
    name = "MLproject",
    author="bhavya",
    install_requires=get_requirements('Requirements.txt')
)