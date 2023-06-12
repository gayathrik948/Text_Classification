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
    column_names:list


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir:Path
    train_file_dir_path:Path
    test_file_dir_path:Path
    tokenizer_name:str
    column_names:list
    custom_model:Path
    custom_model_file:Path

@dataclass(frozen=True)
class ModelPredictionConfig:
    root_dir:Path
    train_file_dir_path:Path
    test_file_dir_path:Path
    column_names: list
    tokenizer_name:str
    model_name:Path
