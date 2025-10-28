import sys
from src.pipeline.training_pipeline import TrainingPipeline
from src.exception import MyException
from src.logger import logging
from src.entity.artifact_entity import DataIngestionArtifact  # adjust import path
import os
import joblib

if __name__ == "__main__":
    try:
        logging.info("======== Stage 02: Data Validation Started ========")
        pipeline = TrainingPipeline()
       
        data_ingestion_artifact = joblib.load("artifact/artifact_objects/data_ingestion.pkl")
        data_validation_artifact=pipeline.start_Data_validation(data_ingestion_artifact)
        os.makedirs("artifact/artifact_objects", exist_ok=True)
        joblib.dump(data_validation_artifact, "artifact/artifact_objects/data_validation.pkl")
        logging.info("======== Stage 02: Data Validation Completed ========")
    except Exception as e:
        logging.error("Error occurred during Data Validation stage")
        raise MyException(e, sys)
