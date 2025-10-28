import sys
from src.pipeline.training_pipeline import TrainingPipeline
from src.exception import MyException
from src.logger import logging
 # adjust import path
import os
import joblib

if __name__ == "__main__":
    try:
        logging.info("======== Stage 02: Data Tranformation Started ========")
        pipeline = TrainingPipeline()
       
        data_ingestion_artifact = joblib.load("artifact/artifact_objects/data_ingestion.pkl")
        data_validation_artifact = joblib.load("artifact/artifact_objects/data_validation.pkl")

        data_transformation_artifact=pipeline.start_Data_transformation(data_validation_artifact,data_ingestion_artifact)
        os.makedirs("artifact/artifact_objects", exist_ok=True)
        joblib.dump(data_transformation_artifact, "artifact/artifact_objects/data_transformation.pkl")
        logging.info("======== Stage 02: Data Tranformation Completed ========")
    except Exception as e:
        logging.error("Error occurred during Data Tranformation stage")
        raise MyException(e, sys)
