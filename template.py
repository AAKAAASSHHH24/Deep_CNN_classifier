"""THIS FILE, template.py HELPS TO AUTO-GENERATE FOLDERS AND GIVE INITIAL STRUCTURE OF THE PROJECT"""

import os
from pathlib import Path  # HELPS CREATE PATH BASED ON THE OPERATING SYSTEM IT IS USED ON (TAKES CARE OF FORWARD AND BACKWARD SLASHES)
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ') #INFO LEVELS HELPS US GET WARNING,CRITICAL AND ERROR AS WELL

package_name = "deepClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",  # gitkeep helps to create the structure even in case of a emplty folder which otherwise might not be pushed
    f"src/{package_name}/__init__.py",   #it classifies the folder as a package
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",  # testing a specific function
    "tests/integration/__init__.py",   #testing the working of an integration such as a pipeline
    "configs/config.yaml",    # contains our configuration
    "dvc.yaml",  # establishes dvc pipeline
    "params.yaml",  # contains training parameters
    "init_setup.sh",  # create environment for the project in shell script
    "requirements.txt",  # requirements
    "requirements_dev.txt",  # requirements for development like black,flake8, pytest
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",   #used for testing the project locally for example testing for different types of OS
    "research/trials.ipynb",  # for testing purpose
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  #in case file path doesnot exist or folder is empty then create a file
        with open(filepath, "w") as f:  #helps to prevent over-writing of file
            pass  # create an empty file
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
