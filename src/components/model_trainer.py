import sys
import os
import json
from src.logger import logging
from src.exception import MyException
from src.utils.main_utils import load_numpy_array_data,load_object,save_object
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from src.constants import *
from src.entity.artifact_entity import MetricArtifact,ModelTrainerArtifact
from src.entity.estimator import My_Model;
import joblib;

class ModelTrainer:
    def __init__(self,data_transformation_artifact,model_trainer_config):
        self.data_transformation_artifact=data_transformation_artifact
        self.model_trainer_config=model_trainer_config

    def get_model_object_and_report(self,trainarr,testarr):
        try:
            logging.info("Training with the random_forest with the specified parameters")
            x_train,y_train,x_test,y_test=trainarr[:,:-1],trainarr[:,-1],testarr[:,:-1],testarr[:,-1]
            print(x_train.shape," ",y_train.shape)
            logging.info("TrainTest Split Done")
            model=RandomForestClassifier(
                n_estimators=MODEL_TRAINER_N_ESTIMATORS,
                min_samples_split=MODEL_TRAINER_MIN_SAMPLE_SPLIT,
                min_samples_leaf=MODEL_TRAINER_MIN_SAMPLE_LEAF,
                max_depth=MIN_SAMPLE_SPLIT_MAX_DEPTH,
                criterion=MIN_SAMPLE_SPLIT_CRITERION
            )
            logging.info("Model Traingng Goinf on")
            model.fit(x_train,y_train)
            logging.info("Model_Trained_Succesfully")
            joblib.dump(model,"artifact/artifact_objects/model.pkl")

            y_pred=model.predict(x_test)
            accuracy=accuracy_score(y_test,y_pred)
            precision=precision_score(y_test,y_pred)
            recall=recall_score(y_test,y_pred)
            f1score=f1_score(y_test,y_pred)

            metric_artifact=MetricArtifact(f1score,precision,recall)
            return model,metric_artifact






        except Exception as e:
            raise MyException(e,sys)

    def initiate_model_trainer(self):
        logging.info("Entered in the Model_Trainer")
        try:
            trainarr=load_numpy_array_data(self.data_transformation_artifact.transformed_train_path)
            testarr=load_numpy_array_data(self.data_transformation_artifact.transformed_test_path)
            logging.info("Train_Test_Loaded")


            trained_model,metric_artifact=self.get_model_object_and_report(trainarr,testarr)
            logging.info("Model_Object_artifact_loaded")
            preprocesser_obj=load_object(self.data_transformation_artifact.transformed_object_path)
            logging.info("Preprocessing object loaded")
            my_model=My_Model(preprocesser_obj,trained_model)
            save_object(self.model_trainer_config.trained_model_file_path,my_model)
            logging.info("Saved Final Model Object with the both preprocessing and trainedmodel")

            model_trainer_artifact=ModelTrainerArtifact(self.model_trainer_config.trained_model_file_path,metric_artifact)
            logging.info("Model_Trainer_artifact")
            metric_report={
                "F1 Score":metric_artifact.f1_score,
                "Precision":metric_artifact.precision_score,
                "Recall":metric_artifact.recall_score
            }

            with open(self.model_trainer_config.trained_model_metrics,'w') as file:
                json.dump(metric_report,file,indent=4)
            return model_trainer_artifact

            


        except Exception as e:
            raise MyException(e,sys)


