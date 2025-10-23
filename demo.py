from src.logger import logging
from src.exception import MyException
import sys


# logging.debug("This is the debug message")
# logging.debug("This is the info message")
# logging.debug("This is the error message")
# logging.debug("This is the Level message")

try:
    a=1+'x'
except Exception as e:
    logging.info(e)
    raise MyException(e,sys) 