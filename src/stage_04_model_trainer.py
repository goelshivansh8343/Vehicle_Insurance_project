import sys
from src.pipeline.training_pipeline import TrainingPipeline
from src.exception import MyException
from src.logger import logging
import sys,os
import joblib

if __name__ == "__main__":
    try:
        logging.info("Model_Training_Get started")
        pipeline=TrainingPipeline()
        data_tranformation_artifact=joblib.load("artifact/artifact_objects/data_transformation.pkl")
        model_trainer_artifact=pipeline.start_model_trainer(data_tranformation_artifact)
        joblib.dump(model_trainer_artifact,"artifact/artifact_objects/model_trainer.pkl")
        

       


        logging.info("Model_Trained_Ended Succesfully")
        

    except Exception as e:
        logging.error("Error occurred during Data Ingestion stage")
        raise MyException(e, sys)
