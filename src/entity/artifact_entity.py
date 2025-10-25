class DataIngestionArtifact:
    def __init__(self, trained_file_path: str, test_file_path: str):
        self.trained_file_path = trained_file_path
        self.test_file_path = test_file_path
        

class DataValidationArtifact:
    def __init__(self,status:bool,message:str,validationreport:str):
        self.validationStatus=status
        self.message=message
        self.validation_report=validationreport

