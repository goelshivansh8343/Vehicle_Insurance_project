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
        

class DataTranformationConfig:
    def __init__(self):
        self.data_transformation_dir=os.path.join(trainingpipelineconfig.artifact_dir,DATA_TRANSFORMATION_DIR_NAME)
        self.tranformed_train_file_path=os.path.join(self.data_transformation_dir,DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,TRAIN_FILE_NAME.replace("csv","npy"))
        self.tranformed_test_file_path=os.path.join(self.data_transformation_dir,DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,TEST_FILE_NAME.replace("csv","npy"))
        self.transformed_object_file_path=os.path.join(self.data_transformation_dir,DATA_TRANSFORMATION_TRANFORMED_OBJECT_DIR,PREPROCSSING_OBJECT_FILE_NAME)
        


class ModelTrainerConfig:
    def __init__(self):
        self.model_trainer_dir=os.path.join(trainingpipelineconfig.artifact_dir,MODEL_TRAINER_DIR_NAME)
        self.trained_model_file_path=os.path.join(self.model_trainer_dir,MODEL_TRAINER_TRAINED_MODEL_DIR,MODEL_TRAINER_TRAINED_MODEL_NAME)
        self.model_config_file_path=MODEL_TRAINER_MODEL_CONFIG_FILE_PATH
        self.n_estimators=MODEL_TRAINER_N_ESTIMATORS
        self.min_samples_split=MODEL_TRAINER_MIN_SAMPLE_SPLIT
        self.min_samples_leaf=MODEL_TRAINER_MIN_SAMPLE_LEAF
        self.max_depth=MIN_SAMPLE_SPLIT_MAX_DEPTH
        self.criterion=MIN_SAMPLE_SPLIT_CRITERION

     



