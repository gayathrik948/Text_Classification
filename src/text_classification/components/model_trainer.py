from text_classification.logging import logging
from text_classification.exceptions import CustomException
from text_classification.components.classf_dataset import CustomDataset
from text_classification.entity import ModelTrainerConfig
from text_classification.utils.common import compute_metrics, _compute_label_mapping
from transformers import Trainer, TrainingArguments
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
import pandas as pd
import sys
import os


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)

    def input_feature_encodings(self):
        try:
            column_names = self.config.column_names
            train_file_dir_path = self.config.train_file_dir_path

            if os.path.exists(train_file_dir_path):
                train_data = pd.read_csv(train_file_dir_path, encoding='latin-1')
                train_input_data = train_data[column_names[0]]
                document = []
                for data in train_input_data:
                    document.append(data)
                targets_data = train_data[column_names[1]]
                targets = []
                for target in targets_data:
                    targets.append(target)
                label2id, id2label = _compute_label_mapping(targets)
                targets = [label2id[target] for target in targets]


                train_encodings = self.tokenizer(
                    document,
                    max_length=64,
                    padding="max_length",
                    truncation=True
                )

                dataset = CustomDataset(train_encodings, targets)
                logging.info('Dataset passed to CustomDataset class successfully')
                return dataset
            else:
                raise CustomException("Train file does not exist.")
        except Exception as e:
            raise CustomException(e, sys)

    def model_training(self):
        try:
            column_names = self.config.column_names
            custom_model = self.config.custom_model
            custom_model_file = self.config.custom_model_file
            train_file_dir_path = self.config.train_file_dir_path

            if os.path.exists(train_file_dir_path):
                train_data = pd.read_csv(train_file_dir_path, encoding='latin-1')
                targets_data = train_data[column_names[1]]
                targets = []
                for target in targets_data:
                    targets.append(target)

                training_args = TrainingArguments(
                    output_dir=custom_model,
                    num_train_epochs=1,
                    evaluation_strategy="no",
                    per_device_train_batch_size=50,
                    warmup_steps=1,
                    weight_decay=0.01,
                    learning_rate=1e-5,
                    lr_scheduler_type="constant",
                    save_strategy="no"
                )

                model = AutoModelForSequenceClassification.from_pretrained(
                    self.config.tokenizer_name,
                    num_labels=len(set(targets))
                )

                trainer = Trainer(
                    model=model,
                    args=training_args,
                    train_dataset=self.input_feature_encodings(),
                    compute_metrics=compute_metrics
                )

            trainer.train()
            logging.info("Training is successfully completed")
            os.makedirs(custom_model_file, exist_ok=True)
            model.save_pretrained(custom_model_file)
            logging.info("Model saving is done")

        except Exception as e:
            raise CustomException(e, sys)
