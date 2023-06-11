from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_url:str
    local_data_file:Path
    unzip_dir:Path
    unzip_dir_file:Path
    train_file_dir:Path
    test_file_dir:Path
    train_file_name:str
    test_file_name:str
    test_size:int