from text_classification.utils.common import *
from text_classification.constants import *
from text_classification.entity import (DataIngestionConfig,
ModelTrainerConfig,ModelPredictionConfig)



class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILEPATH,
                        params_filepath=PARAMS_FILEPATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
                                                    root_dir=config.root_dir,
                                                    source_url=config.source_url,
                                                    local_data_file=config.local_data_file,
                                                    unzip_dir=config.unzip_dir,
                                                    unzip_dir_file=config.unzip_dir_file,
                                                    train_file_dir=config.train_file_dir,
                                                    test_file_dir=config.test_file_dir,
                                                    test_size=config.test_size,
                                                    train_file_name=config.train_file_name,
                                                    test_file_name=config.test_file_name,
                                                    column_names=config.column_names,
                                                    )
        return data_ingestion_config


    def get_model_trainer(self)->ModelTrainerConfig:
        config = self.config.model_trainer
        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
                                                        root_dir=config.root_dir,
                                                        train_file_dir_path=config.train_file_dir_path,
                                                        test_file_dir_path=config.test_file_dir_path,
                                                        tokenizer_name=config.tokenizer_name,
                                                        column_names=config.column_names,
                                                        custom_model=config.custom_model,
                                                        custom_model_file=config.custom_model_file)
        return model_trainer_config


    def get_model_Prediction(self)->ModelPredictionConfig:
        config = self.config.model_prediction
        create_directories([config.root_dir])

        model_prediction_config = ModelPredictionConfig(
                                                    root_dir=config.root_dir,
                                                    tokenizer_name=config.tokenizer_name,
                                                    model_name=config.model_name,
                                                    train_file_dir_path=config.train_file_dir_path,
                                                    test_file_dir_path=config.test_file_dir_path,
                                                    column_names=config.column_names
        )
        return model_prediction_config