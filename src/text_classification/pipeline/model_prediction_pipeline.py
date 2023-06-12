from text_classification.config.configuration import ConfigurationManager
from text_classification.components.model_prediction import ModelPrediction


class ModelPredictionPipeline:
    def __init__(self):
        pass

    def modelpredictionpipeline(self):
        config = ConfigurationManager()
        model_prediction_config = config.get_model_Prediction()
        model_prediction = ModelPrediction(config=model_prediction_config)
        text = 'top round steak vegetable oil shiitake soy sauce fresh asparagus green onions'
        model_prediction.predict(text=text)