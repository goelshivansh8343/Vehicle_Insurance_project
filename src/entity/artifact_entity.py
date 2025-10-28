import pickle
import os
class DataIngestionArtifact:
    def __init__(self, trained_file_path: str, test_file_path: str):
        self.trained_file_path = trained_file_path
        self.test_file_path = test_file_path
    @staticmethod
    def save(self, file_path: str):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(file_path: str):
        with open(file_path, 'rb') as f:
            return pickle.load(f)
        

class DataValidationArtifact:
    def __init__(self,status:bool,message:str,validationreport:str):
        self.validationStatus=status
        self.message=message
        self.validation_report=validationreport


class DataTransformationArtifact:
    def __init__(self,transformed_object_path,transformed_train_path,transformed_test_path):
        self.transformed_object_path=transformed_object_path
        self.transformed_train_path=transformed_train_path
        self.transformed_test_path=transformed_test_path


class MetricArtifact:
    def __init__(self,f1_score,precision_score,recall_score):
        self.f1_score=f1_score
        self.precision_score=precision_score
        self.recall_score=recall_score

class ModelTrainerArtifact:
    def __init__(self,trained_model_path,metric_artifact):
        self.trained_model_path=trained_model_path
        self.metric_artifact=metric_artifact
    


