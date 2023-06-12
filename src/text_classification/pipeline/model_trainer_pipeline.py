from text_classification.components.model_trainer import ModelTrainer
from text_classification.config.configuration import ConfigurationManager


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def modeltrainerpipeline(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.input_feature_encodings()
        model_trainer.model_training()
