from text_classification.logging import logging
import zipfile
from text_classification.config.configuration import DataIngestionConfig
from text_classification.utils.common import get_size, _compute_label_mapping
from text_classification.exceptions import CustomException
from sklearn.model_selection import train_test_split
import urllib.request as request
import os, sys
import pandas as pd


class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename , headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logging.info(f"{filename} successfully saved the url")
        else:
            logging.info(f"{self.config.local_data_file} is already exists and size is {get_size(self.config.local_data_file)}")

    def unzip_data(self):
        unzip_data = self.config.unzip_dir
        os.makedirs(unzip_data, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_file:
            zip_file.extractall(unzip_data)
            logging.info(f'Successfully unzipped the data, and save into directory')

    # def label_encoding(self):
    #
    #     raw_file = self.config.unzip_dir_file
    #     column_names = self.config.column_names
    #     label_encoded_dir = self.config.label_encoded_dir
    #     label_encoded_name = self.config.label_encoded_name
    #
    #     if not os.path.exists(raw_file):
    #         self.unzip_data()
    #
    #     raw_data = pd.read_csv(raw_file, encoding='latin-1')
    #     label2id = _compute_label_mapping(raw_data[column_names[1]])[0]
    #     raw_data[column_names[1]] = [label2id[label] for label in raw_data[column_names[1]]]
    #
    #     os.makedirs(label_encoded_dir, exist_ok=True)
    #     label_encoded_file_path = os.path.join(label_encoded_dir, label_encoded_name)
    #     raw_data.to_csv(label_encoded_file_path, index=False)




    def train_test_split(self):
        try:
            raw_file = self.config.unzip_dir_file
            train_file_dir = self.config.train_file_dir
            test_file_dir = self.config.test_file_dir
            train_file_name = self.config.train_file_name
            test_file_name = self.config.test_file_name


            if not os.path.exists(raw_file):
                self.unzip_data()


            raw_data = pd.read_csv(raw_file, encoding='latin-1')

            train_data, test_data = train_test_split(raw_data, test_size=self.config.test_size)

            os.makedirs(train_file_dir, exist_ok=True)
            train_file_path = os.path.join(train_file_dir, train_file_name)
            train_data.to_csv(train_file_path, index=False)

            os.makedirs(test_file_dir, exist_ok=True)
            test_file_path = os.path.join(test_file_dir, test_file_name)
            test_data.to_csv(test_file_path, index=False)

            logging.info(f"csv file exist and succesfully converted train & test files")
        except Exception as e:
            logging.info(f"no csv file exist")
            raise CustomException(e,sys)










