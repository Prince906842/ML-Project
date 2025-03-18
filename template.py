import logging.config
import os 
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO) 

projectname = "mlproject" 

list_of_files = [
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/components/data_ingestions.py",
    f"src/components/data_transformations.py",
    f"src/components/model_trainer.py",
    f"src/components/model_monitering.py",
    f"src/pipelines/__init__.py",
    f"src/pipelines/training_pipeline.py",
    f"src/pipelines/prediction_pipeline.py",
    f"src/exception.py",
    f"src/logger.py",
    f"src/utils.py",
    "app.py",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")