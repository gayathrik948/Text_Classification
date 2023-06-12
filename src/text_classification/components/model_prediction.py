from text_classification.exceptions import CustomException
from text_classification.entity import ModelPredictionConfig
from text_classification.logging import logging
import torch, os, sys
import pandas as pd
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
from text_classification.utils.common import _compute_label_mapping

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


class ModelPrediction:
    def __init__(self, config: ModelPredictionConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(config.model_name)

    def predict(self, text):
        try:
            column_names = self.config.column_names
            train_file_dir_path = self.config.train_file_dir_path

            targets = []
            if os.path.exists(train_file_dir_path):
                train_data = pd.read_csv(train_file_dir_path, encoding='latin-1')
                targets_data = train_data[column_names[1]]
                targets = targets_data.tolist()

            inputs = self.tokenizer(
                text,
                padding="max_length",
                max_length=64,
                truncation=True,
                return_tensors="pt",
            )

            outputs = self.model(**inputs)
            label2id, id2label = _compute_label_mapping(targets)
            prediction = id2label[int(outputs["logits"][0].argmax())]
            logging.info(f'{prediction} successfully done')
            print(prediction)
            return prediction

        except Exception as e:
            raise CustomException(str(e), sys.exc_info())








