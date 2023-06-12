from text_classification.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from text_classification.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from  text_classification.pipeline.model_prediction_pipeline import ModelPredictionPipeline
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



STAGE_NAME = "MODEL_TRAINING"

try:
    logging.info(f"{STAGE_NAME} is started")

    model_training = ModelTrainerPipeline()
    model_training.modeltrainerpipeline()

    logging.info(f"{STAGE_NAME} is completed")

except Exception as e:
    logging.info(e)
    raise CustomException(e, sys)




STAGE_NAME = "MODEL_PREDICTION"

try:
    logging.info(f"{STAGE_NAME} is started")
    model_prediction = ModelPredictionPipeline()
    model_prediction.modelpredictionpipeline()

    logging.info(f"{STAGE_NAME} is completed")

except Exception as e:
    logging.info(e)
    raise CustomException(e, sys)