from ensure import ensure_annotations
from text_classification.logging import logging
from text_classification.exceptions import CustomException
from box import ConfigBox
from box.exceptions import BoxValueError
import os, sys
import yaml
from pathlib import Path
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import precision_recall_fscore_support, accuracy_score



@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"{path_to_yaml} is loaded Successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise CustomException(e, sys)


@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    for file_path in path_to_directories:
        os.makedirs(file_path, exist_ok=True)
        if verbose:
            logging.info(f"{file_path} created directory successfully")



@ensure_annotations
def get_size(path:Path):
    size_in_kb = round(len(os.path.getsize(path)/1024))
    return f'{size_in_kb}KB'


@ensure_annotations
def _compute_label_mapping(labels):
    """
    Maps the labels to integers and stores them in the class attributes.
    """

    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(labels)
    label2id = {}
    id2label = {}
    for label in np.unique(labels):
        label2id[label] = int(label_encoder.transform([label])[0])
    for i in integer_encoded:
        id2label[int(i)] = label_encoder.inverse_transform([i])[0]
    return label2id, id2label


@ensure_annotations
def compute_metrics(pred):
    """
    Helper function to compute aggregated metrics from predictions.
    """
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    precision, recall, f1, _ = precision_recall_fscore_support(
        labels, preds, average="weighted"
    )
    acc = accuracy_score(labels, preds)
    return {"accuracy": acc, "f1": f1, "precision": precision, "recall": recall}
