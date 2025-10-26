class DataIngestionArtifact:
    def __init__(self, trained_file_path: str, test_file_path: str):
        self.trained_file_path = trained_file_path
        self.test_file_path = test_file_path
        

class DataValidationArtifact:
    def __init__(self,status:bool,message:str,validationreport:str):
        self.validationStatus=status
        self.message=message
        self.validation_report=validationreport


class DataTranformationArtifact:
    def __init__(self,tranformed_object_path,tranformed_train_path,tranformed_test_path):
        self.tranformed_object_path=tranformed_object_path
        self.tranformed_train_path=tranformed_train_path
        self.tranformed_test_path=tranformed_test_path


class MetricArtifact:
    def __init__(self,f1_score,precision_score,recall_score):
        self.f1_score=f1_score
        self.precision_score=precision_score
        self.recall_score=recall_score

class ModelTrainerArtifact:
    def __init__(self,trained_model_path,metric_artifact):
        self.trained_model_path=trained_model_path
        self.metric_artifact=metric_artifact
    


