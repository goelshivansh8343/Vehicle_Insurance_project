import sys
from src.pipeline.training_pipeline import TrainingPipeline
from src.exception import MyException
from src.logger import logging
import sys,os
import joblib

if __name__ == "__main__":
    try:
        logging.info("======== Stage 01: Data Ingestion Started ========")
        
        pipeline = TrainingPipeline()
        data_ingestion_artifact = pipeline.start_Data_ingestion()
        os.makedirs("artifact/artifact_objects", exist_ok=True)
        joblib.dump(data_ingestion_artifact, "artifact/artifact_objects/data_ingestion.pkl")
        

    except Exception as e:
        logging.error("Error occurred during Data Ingestion stage")
        raise MyException(e, sys)
