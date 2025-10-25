import os
import sys
from src.logger import logging
from src.exception import MyException
import yaml
import pandas as pd
import numpy as  np



def read_yaml_file(filepath:str):
    try:
        with open(filepath,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise MyException(e,sys)
    

