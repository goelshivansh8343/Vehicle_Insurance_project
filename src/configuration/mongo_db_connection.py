# The purpose of thei file to fetch the data form the database
import os
from src.logger import logging
from src.exception import MyException
import pymongo
import sys
from src.constants import MONGODB_URL

# The MongoDb client is basically usefull for establising the connectiion with the database


class MongoDBClient:
    client=None
    def __init__(self,dataname:str)->None:
        try:
            if MongoDBClient.client is None:
                mongodburl=MONGODB_URL
                if(mongodburl is None):
                    raise Exception(f"Enviroment Varable {MONGODB_URL} is not SET")
                MongoDBClient.client=pymongo.MongoClient(mongodburl)

            self.client=MongoDBClient.client
            self.database=self.client[dataname]
            self.database_name=dataname
            logging.info("Mongo DB Connection is succesfully set")

        except Exception as e:
            raise MyException(e,sys)
    


        


