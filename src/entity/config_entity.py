import os
from datetime import datetime
from src.constants import *

TIMESTAMP=datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

class TrainingPipelineConfig:
    def __init__(self):
        self.pipeline_name=PIPELINE_NAME
        self.artifact_dir=os.path.join(ARTIFACT_DIR,TIMESTAMP)



trainingpipelineconfig=TrainingPipelineConfig()


class DataIngestionConfig:
    def __init__(self):
        self.data_ingestion_dir=os.path.join(trainingpipelineconfig.artifact_dir,DATA_INGESTION_DIR_NAME)
        self.feature_store_file_name=os.path.join(self.data_ingestion_dir,DATA_INGESTION_FEATURE_STORE_DIR,FILE_NAME)
        self.training_file_path=os.path.join(self.data_ingestion_dir,DATA_INGESTION_INGESTED_DIR,TRAIN_FILE_NAME)
        self.testing_file_path=os.path.join(self.data_ingestion_dir,DATA_INGESTION_INGESTED_DIR,TEST_FILE_NAME)
        self.train_test_split=DATA_INGESTION_TRAIN_TEST_RATIO


    
class DataValidationConfig:
    def __init__(self):
        self.data_validation_dir=os.path.join(trainingpipelineconfig.artifact_dir,DATA_VALIDATION_DIR_NAME)
        self.data_validation_report_file_path=os.path.join(self.data_validation_dir,DATA_VALIDATION_FILE_NAME)
        