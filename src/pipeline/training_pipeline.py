import sys
import os
from src.logger import logging
from src.exception import MyException
from src.entity.config_entity import DataIngestionConfig
from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataValidationConfig
from src.components.data_validation import DataValidation
from src.entity.artifact_entity import DataIngestionArtifact



class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
        self.data_validation_config=DataValidationConfig()


    def start_Data_ingestion(self):
        try:
            logging.info("Entered into the Data_Ingestion_part")
            logging.info("Gettig the Data fom mongo_db")
            data_ingestion=DataIngestion(self.data_ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info("Got the Train and_test split from the MongoDB")
            logging.info("Exicted from the Data ingestion class")
            return data_ingestion_artifact
        except Exception as e:
            raise MyException(e,sys)
        
    def start_Data_validation(self,data_ingestion_artifact):
        logging.info("Entered into the Data_Validation_part")
        try:
            data_validation=DataValidation(self.data_validation_config,data_ingestion_artifact)
            data_validation_artifact=data_validation.initiate_data_validation()
            logging.info("Performed the data validation operation")
            logging.info("Exited the start_data_validation method of TrainPipeline class")

            return data_validation_artifact
        except Exception as e:
            raise MyException(e,sys)
        

            



    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_Data_ingestion()
            data_validation_artifact=self.start_Data_validation(data_ingestion_artifact)
        except Exception as e:
            raise MyException(e,sys)
        

