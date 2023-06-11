from text_classification.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from text_classification.logging import logging
from text_classification.exceptions import CustomException
import sys

STAGE_NAME = "DATA_INGESTION"

try:
    logging.info(f"{STAGE_NAME} is started")

    data_ingestion = DataIngestionPipeline()
    data_ingestion.dataingestionpipeline()

    logging.info(f"{STAGE_NAME} is completed")



except Exception as e:
    logging.info(e)
    raise CustomException(e, sys)




