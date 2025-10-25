import os
import json
import sys
from src.logger import logging
from src.exception import MyException
from src.constants import SCHEMA_FILE_PATH
from src.utils.main_utils import read_yaml_file
from src.entity.config_entity import DataValidationConfig
from src.entity.artifact_entity import DataValidationArtifact,DataIngestionArtifact
import pandas as pd


class DataValidation:
    def __init__(self,data_validation_config,data_ingestion_artifact):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self.schema_config=read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise MyException(e,sys)
        
    @staticmethod
    def read_file(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise MyException(e,sys)

    def validate_number_of_columns(self,dataframe)->bool:
        try:
            status=len(dataframe.columns)==len(self.schema_config["columns"])
            logging.info(f"Is the required Columns Present {status}")
            return status
        except Exception as e:
            raise MyException(e,sys)
        
    def is_column_exist(self,dataframe)->bool:
        try:
            df_columns=dataframe.columns
            missing_numerical=[]
            missing_categorical=[]
            for col in self.schema_config["numerical_columns"]:
                if col not in df_columns:
                    missing_numerical.append(col)

            if(len(missing_numerical)>0):
                logging.info(f"We have miised some numerical columns {missing_numerical}")

            for col in self.schema_config["categorical_columns"]:
                if col not in df_columns:
                    missing_categorical.append(col)

            if(len(missing_categorical))>0:
                logging.info(f"Catetorical Columns is missing {missing_categorical}")

            return False if len(missing_categorical)>0 or len(missing_numerical)>0 else True
        

        except Exception as e:
            raise MyException(e,sys)
        



            
    def initiate_data_validation(self):
        try:
            validation_error_message=""
            logging.info("The Data validation basically stoarted")
            traindf,testdf=(DataValidation.read_file(self.data_ingestion_artifact.trained_file_path),(DataValidation.read_file(self.data_ingestion_artifact.test_file_path)))


            status=self.validate_number_of_columns(traindf)
            if not status:
                validation_error_message+="Columns are missing Bro in traing"
            else:
                logging.info(f"All the columns are basically present in traing")
            
            status=self.validate_number_of_columns(traindf)
            if not status:
                validation_error_message+="Columns are missing Bro in testing"
            else:
                logging.info(f"All the columns are basically present in testing")

            status=self.is_column_exist(traindf)

            if not status:
                validation_error_message+="Columns in missing in the trainf"
            else:
                logging.info("All Set")


            status=self.is_column_exist(testdf)
            if not status:
                validation_error_message+="Columns in missing in the testdf"
            else:
                logging.info("All Set")


            validation_status=len(validation_error_message)==0
            data_validation_artifact=DataValidationArtifact(validation_status,validation_error_message,self.data_validation_config.data_validation_report_file_path)


            report_dir=os.path.dirname(self.data_validation_config.data_validation_report_file_path)
            os.makedirs(report_dir,exist_ok=True)

            validation_report={
                "Validation status":validation_status,
                "message":validation_error_message.strip()
            }

            with open(self.data_validation_config.data_validation_report_file_path,'w') as file:
                json.dump(validation_report,file,indent=4)


            logging.info("Data validation artifact created and saved to JSON file.")
            logging.info(f"Data validation artifact: {data_validation_artifact}")
            return data_validation_artifact
        
        except Exception as e:
            raise MyException(e,sys)
        


            





        