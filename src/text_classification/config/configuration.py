from text_classification.utils.common import *
from text_classification.constants import *
from text_classification.entity import DataIngestionConfig



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
                                                    test_file_name=config.test_file_name
                                                    )
        return data_ingestion_config
