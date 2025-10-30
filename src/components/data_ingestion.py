import os
from src.logger import logging
from src.exception import MyException
from src.data_access.proj1_data import proj1Data
import sys
from src.entity.artifact_entity import DataIngestionArtifact
from src.entity.config_entity import DataIngestionConfig
from sklearn.model_selection import train_test_split
import pandas as pd
from src.constants import COLLECTION_NAME


class DataIngestion:
    def __init__(self,Data_ingestion_config):
        try:
            self.data_ingestion_config=Data_ingestion_config
        except Exception as e:
            raise MyException(e,sys)
        
    def export_data_into_feature_store(self):
        try:
            logging.info("Enposrting the data from the mongodb database")
            my_data=proj1Data()
            df=my_data.export_collection_as_dataframe(COLLECTION_NAME)
            logging.info(f"Shape of the dataframe {df.shape}")
            feature_store_file_path=self.data_ingestion_config.feature_store_file_name
            dir_name=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_name,exist_ok=True)
            logging.info(f"Saving the Exported file from the mondodb to the StoredFilePath {feature_store_file_path}")
            df.to_csv(feature_store_file_path,index=False,header=True)
            return df
        except Exception as e:
            raise MyException(e,sys)
        

    def split_data_as_train_test_split(self, dataframe)->None:
        try:
            logging.info("Entered into the train_test_split for the spliting of the data")
            train_set,test_set=train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split)
            logging.info("Performed the train_test_split Succesfully")
            logging.info("Exixted from the train_test_split")


            train_dir=os.path.dirname(self.data_ingestion_config.training_file_path)
            test_dir=os.path.dirname(self.data_ingestion_config.testing_file_path)
            os.makedirs(test_dir,exist_ok=True)
            os.makedirs(train_dir,exist_ok=True)

            logging.info("Exporting the train_ans_test_split")
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)
            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)

            logging.info("Exported the Train test split path")
        except Exception as e:
            raise MyException(e,sys)
        

    def initiate_data_ingestion(self)->DataIngestionArtifact:
        logging.info("Entered_initiate inthe data_ingestion_project")
        try:
            dataframe=self.export_data_into_feature_store()
            logging.info("Got the data from the mongodb")
            self.split_data_as_train_test_split(dataframe)
            logging.info("Performed the train_test_split")
            logging.info("Exiceted from the data_ingestion_part")
            Data_ingestion_artifact=DataIngestionArtifact(self.data_ingestion_config.training_file_path,self.data_ingestion_config.testing_file_path)
            logging.info("Artifact saved at the DATAIngestionArtifcet ans succesfully Done")
            return Data_ingestion_artifact
        except Exception as e:
            raise MyException(e,sys)

    
                     





