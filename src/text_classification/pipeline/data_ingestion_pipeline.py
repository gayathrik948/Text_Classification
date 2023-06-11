from text_classification.components.data_ingestion import DataIngestion
from text_classification.config.configuration import ConfigurationManager


class DataIngestionPipeline:
    def __init__(self):
        pass

    def dataingestionpipeline(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.unzip_data()
        data_ingestion.train_test_split()