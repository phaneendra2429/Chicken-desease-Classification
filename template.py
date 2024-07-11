import os
from pathlib import Path
import logging

# This line is used for logging Configuration which is used for debugging and monitoring information logging time stamping consistency and standardization accountability and auditing
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:]')

project_name="cnnClassifier"


# The Below code is used to set up all the Folders packages and files configurations required for the project
list_of_files = [
".github/workflows/.gitkeep",
f"sec/{project_name}/__init__.py",
f"sec/{project_name}/components/__init__.py",
f"sec/{project_name}/utils/__init__.py",
f"sec/{project_name}/config/__init__.py",
f"sec/{project_name}/config/configuration.py",
f"sec/{project_name}/pipeline/__init__.py",
f"sec/{project_name}/entity/__init__.py",
f"sec/{project_name}/constants/__init__.py",
"config/config.yaml",
"dvc.yaml",
"requirements.txt",
"setup.py",
"research/trails.ipynb"



]


# This line of code is used to rectify the error of \ and / in file paths for Windows
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
