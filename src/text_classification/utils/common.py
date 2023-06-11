from ensure import ensure_annotations
from src.text_classification.logging import logging
from src.text_classification.exceptions import CustomException
from box import ConfigBox
import os, sys
import yaml
from pathlib import Path



@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"{path_to_yaml} is loaded Successfully")
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e, sys)


@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    for file_path in path_to_directories:
        os.makedirs(file_path, exist_ok=True)
        if verbose:
            logging.info(f"{file_path} created directory successfully")



@ensure_annotations
def get_size(path:Path):
    size_in_kb = round(len(os.path.getsize(path)/1024))
    return f'{size_in_kb}KB'

