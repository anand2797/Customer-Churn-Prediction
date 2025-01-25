import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]- [%(message)s]")

project_name = "Customet_churn_prediction"

files = [
         f"src/{project_name}/__init__.py",
         f"src/{project_name}/components/__init__.py",

         f"src/{project_name}/utils/__init__.py",
         f"src/{project_name}/utils/common.py",
         f"src/{project_name}/utils/s3_utils.py",


         f"src/{project_name}/config/__init__.py",
         f"src/{project_name}/config/configuration.py",

         f"src/{project_name}/pipeline/__init__.py",

         f"src/{project_name}/entity/__init__.py",
         f"src/{project_name}/entity/config_entity.py",

         f"src/{project_name}/constants/__init__.py",
         
         ".env",
         "main.py",
         "requirements.txt",
         "app.py",
         "research/notebooks/research.ipynb",
         "setup.py",
         "templates/index.html"

]

for filepath in files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)  # this line split the filepath and return file directory and filename 

    # 
    if filedir != '':
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"Creating directory '{filedir}' - for file '{filename}'.")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as file:
            pass
            logging.info(f"Creating a empty file : {filepath}.")

    else:
        logging.info(f"{filename} is already exists.")



