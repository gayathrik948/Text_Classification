from pathlib import Path
import os
import logging

project = 'text-classification'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project}/__init__.py",
    f"src/{project}/utils/__init__.py",
    f"src/{project}/logging/__init__.py",
    f"src/{project}/exceptions/__init__.py",
    f"src/{project}/components/__init__.py",
    f"src/{project}/pipeline/__init__.py",
    f"src/{project}/config/__init__.py",
    f"src/{project}/config/configuration.py",
    f"src/{project}/entity/__init__.py",
    f"src/{project}/constants/__init__py",
    "setup.py",
    "requirements.txt",
    "config/config.yaml",
    "params.yaml",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if not (os.path.exists(filepath)) or (os.path.getsize(filepath)) == 0:
        with open(filepath, 'w') as f:
            pass
    else:
        logging.info(f'{filepath} already exists')
