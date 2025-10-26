import sys
import os
from src.logger import logging
from src.exception import MyException
from src.entity.config_entity import DataIngestionConfig
from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataValidationConfig
from src.components.data_validation import DataValidation
from src.entity.config_entity import DataTranformationConfig
from src.components.data_transformation import DataTransformation
from src.entity.config_entity import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
        self.data_validation_config=DataValidationConfig()
        self.data_tranformation_config=DataTranformationConfig()
        self.data_model_trainer_config=ModelTrainerConfig()



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
        

    def rename_columns(self,df):
        try:
            logging.info("Entered into the renaming of the columns")
            df = df.rename(columns={
            "Vehicle_Age_< 1 Year": "Vehicle_Age_lt_1_Year",
            "Vehicle_Age_> 2 Years": "Vehicle_Age_gt_2_Years"
             })
            return df
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
        

    def start_Data_tranformation(self,data_validation_artifact,data_ingestion_artifact):
        try:
            logging.info("Entered into the Data_Tranformation_step")
            data_tranformation=DataTransformation(self.data_tranformation_config,data_validation_artifact,data_ingestion_artifact)
            data_tranformation_artifact=data_tranformation.initiate_data_tranformation()
            logging.info("Performed the Data  tranformation operation")
            logging.info("Exited from thr data_tranformation_method")

            return data_tranformation_artifact
        except Exception as e:
            raise MyException(e,sys)
        

    def start_model_trainer(self,data_transformation_artifact):
        try:
            logging.info("Entered into the the model_trainer_module")
            model_trainer=ModelTrainer(data_transformation_artifact,self.data_model_trainer_config)
            model_trainer_artifact=model_trainer.initiate_model_trainer()

            return model_trainer_artifact
        except Exception as e:
            raise MyException(e,sys)
        
        


        

            



    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_Data_ingestion()
            data_validation_artifact=self.start_Data_validation(data_ingestion_artifact)
            data_tranformation_artifact=self.start_Data_tranformation(data_validation_artifact,data_ingestion_artifact)
            model_trainer_artifact=self.start_model_trainer(data_tranformation_artifact)

        except Exception as e:
            raise MyException(e,sys)
        

