# This will be fetching the data from the mongodb
import sys
from src.constants import DATABASE_NAME
import numpy as np
import pandas as pd
from src.configuration.mongo_db_connection import MongoDBClient
from src.exception import MyException
from src.logger import logging

class proj1Data:
    def __init__(self):
        try:
            self.mongodbclient=MongoDBClient(DATABASE_NAME)
        except Exception as e:
            raise MyException(e,sys)
        

    def export_collection_as_dataframe(self,collection_name:str)->pd.DataFrame:
        collection=self.mongodbclient.database[collection_name]
        print("Fetching Data from the MongoDB")
        df=pd.DataFrame(list(collection.find()))
        df.drop("_id",axis=1,inplace=True)
        return df


