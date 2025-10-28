import sys
import os
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import MyException


class My_Model:
    def __init__(self,preprocessor_object,trained_model_object):
        self.preprocessor=preprocessor_object
        self.trained_model=trained_model_object


        
        
