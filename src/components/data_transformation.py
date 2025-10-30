from src.logger import logging
from src.exception import MyException
import os
import sys
import pandas as pd
import numpy as np
from src.constants import SCHEMA_FILE_PATH
from src.utils.main_utils import read_yaml_file,save_object,save_numpy_array_data
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from imblearn.combine import SMOTEENN
from src.entity.artifact_entity import DataTransformationArtifact
import joblib

class DataTransformation:
    def __init__(self,data_transformation_config,data_validation_artifact,data_ingestion_artifact):
        self.data_transformation_config=data_transformation_config
        self.data_validation_artifact=data_validation_artifact
        self.data_ingestion_artifact=data_ingestion_artifact
        self._shema_config=read_yaml_file(SCHEMA_FILE_PATH)


    @staticmethod
    def read_data(filepath)->pd.DataFrame:
        try:
            df=pd.read_csv(filepath)
            df.columns=df.columns.str.strip()
            return df
        except Exception as e:
            raise MyException(e,sys)
        
    def map_gender_column(self,data)->pd.DataFrame:
        try:
            lbd=LabelEncoder()
            data["Gender"]=lbd.fit_transform(data["Gender"])
            return data
        except Exception as e:
            raise MyException(e,sys)
        

    def drop_id(self,data)->pd.DataFrame:
        try:
            data.drop("id",axis=1,inplace=True)
            return data
        except Exception as e:
            raise MyException(e,sys)
    
    def map_vehicle_damage(self,data)->pd.DataFrame:
        try:
            lbd=LabelEncoder()
            data["Vehicle_Damage"]=lbd.fit_transform(data["Vehicle_Damage"])
            

            return data
        except Exception as e:
            raise MyException(e,sys)
        

    def create_dummy_columns(self,data)->pd.DataFrame:
        try:
            dummies = pd.get_dummies(data["Vehicle_Age"], drop_first=True)
            data = pd.concat([data, dummies], axis=1)
            data.drop("Vehicle_Age", axis=1, inplace=True)
            return data
        except Exception as e:
            raise MyException(e,sys)
        
    def outliers(self,data)->pd.DataFrame:
        try:
            q1=np.quantile(data["Annual_Premium"],0.25)
            q3=np.quantile(data["Annual_Premium"],0.75)
            IQR=q3-q1
            upper=q3+1.5*IQR
            lower=q1-1.5*IQR
            data["Annual_Premium"]=np.where(data["Annual_Premium"]>upper,upper,np.where(data["Annual_Premium"]<lower,lower,data["Annual_Premium"]))
            return data
        except Exception as e:
            raise MyException(e,sys)
        

    def get_data_transformer_object(self)->Pipeline:
        try:
            logging.info("Entered into the DataTranformation")
            numeric_tranfomer=StandardScaler()
            min_max=MinMaxScaler()

            num_features=self._shema_config["num_features"]
            mm_columns=self._shema_config["mm_columns"]

            logging.info("Columns lodded from the schema")

            preprocessor=ColumnTransformer(transformers=[("Standard_Scaler",numeric_tranfomer,num_features),("Min_MAX_Scaler",min_max,mm_columns)],remainder='passthrough')
            final_pipeline=Pipeline([("Preprocessor",preprocessor)])
            logging.info("Final_Pipeline set")
            return final_pipeline
        except Exception as e:
            raise MyException(e,sys)
        




    def initiate_data_transformation(self):
        try:
            logging.info("Data_Transformation_Started")
            if self.data_validation_artifact.validationStatus==False:
                raise Exception(self.data_validation_artifact.message)
            
            logging.info("Loading the Train and test data")
            train_df=DataTransformation.read_data(self.data_ingestion_artifact.trained_file_path)
            test_df=DataTransformation.read_data(self.data_ingestion_artifact.test_file_path)
            logging.info("Test and train Datafrane data fetched Succesfully")


            input_feature_traindf=train_df.drop("Response",axis=1)
            target_feature_traindf=train_df["Response"]


            input_feature_testdf=test_df.drop("Response",axis=1)
            target_feature_testdf=test_df["Response"]

            logging.info("Input and the target columsn defined for the both input and the output columns")

            input_feature_traindf=self.map_gender_column(input_feature_traindf)
            input_feature_testdf=self.map_gender_column(input_feature_testdf)

            logging.info("Gender Columns maped successfullyy")

            input_feature_traindf=self.drop_id(input_feature_traindf)
            input_feature_testdf=self.drop_id(input_feature_testdf)

            logging.info("Id Columns Dropped Succesfully")
            
            input_feature_traindf=self.map_vehicle_damage(input_feature_traindf)
            input_feature_testdf=self.map_vehicle_damage(input_feature_testdf)

            logging.info("Vehicle Columns mapped Succesfully")


            input_feature_traindf=self.create_dummy_columns(input_feature_traindf)
            input_feature_testdf=self.create_dummy_columns(input_feature_testdf)

            logging.info("Dummy_Columns  Succewfully created")

            logging.info("Stareted the data tranformation")

            preprocessor=self.get_data_transformer_object()
            logging.info("We got the preprocessor onhect")
            print("Columns in train dataframe:", input_feature_traindf.columns.tolist())
            print("The values in the array is given by the ")
            print(input_feature_traindf.head())
            print(input_feature_traindf["Gender"])
            print(input_feature_traindf["Age"])
            print(input_feature_traindf["Driving_License"])
            print(input_feature_traindf["Region_Code"])
            print(input_feature_traindf["Previously_Insured"])
            print(input_feature_traindf["Vehicle_Damage"])
            print(input_feature_traindf["Annual_Premium"])
            print(input_feature_traindf["Policy_Sales_Channel"])
            print(input_feature_traindf["Vintage"])
            print(input_feature_traindf["< 1 Year"])
            print(input_feature_traindf["> 2 Years"])
            



            logging.info("Initializing for the Traing data")
            input_feature_train_arr=preprocessor.fit_transform(input_feature_traindf)
            input_feature_test_arr=preprocessor.fit_transform(input_feature_testdf)
            logging.info("Tranformation done end to end")
            # Get transformed column names
            columns = ['Gender', 'Age', 'Driving_License', 'Region_Code', 'Previously_Insured',
            'Vehicle_Damage', 'Annual_Premium', 'Policy_Sales_Channel', 'Vintage',
            '< 1 Year', '> 2 Years']

            values = [[1, 35, 1, 28.0, 0, 1, 35000.0, 152.0, 120, True, False]]

            input_df = pd.DataFrame(values, columns=columns)
            print("Akhil")
            print(input_df)
            logging.info("Checking Preprocessing")
            try:
                preprocessor.fit_transform(input_df)
            except Exception as e:
                raise MyException(e,sys)
            

            joblib.dump(preprocessor,"artifact/artifact_objects/preprocessor.pkl")



            logging.info("Applying the Smooting techinqueue")
            smt=SMOTEENN(sampling_strategy='minority')
            input_feature_train_final,target_feature_train_final=smt.fit_resample(input_feature_train_arr,target_feature_traindf)
            input_feature_test_final,target_feature_test_final=smt.fit_resample(input_feature_test_arr,target_feature_testdf)
            logging.info("Smote Applied Succesfully")

            train_arr=np.c_[input_feature_train_final,np.array(target_feature_train_final)]
            test_arr=np.c_[input_feature_test_final,np.array(target_feature_test_final)]
            
            logging.info("Feature Target Consction Done")

            save_object(self.data_transformation_config.transformed_object_file_path,preprocessor)
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path,train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path,test_arr)


            logging.info("Saving Transformation objext Saved")
            logging.info("Data Transformation completeflt implelemted")

            return DataTransformationArtifact(self.data_transformation_config.transformed_object_file_path,self.data_transformation_config.transformed_train_file_path,self.data_transformation_config.transformed_test_file_path)




        except Exception as e:
            raise MyException(e,sys)
        




                
            


    
