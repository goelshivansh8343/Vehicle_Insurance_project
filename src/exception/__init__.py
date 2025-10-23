import sys  # this gives us the system related information
import logging


def error_message_detail(error:Exception,error_detail:sys)->str:
    _,_,exc_tb=error_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    linenumber=exc_tb.tb_lineno
    error_message=f"Error ocuured in the python script : [{filename}] at line_number [{linenumber}]: {str(error)}"
    logging.error(error_message)
    return error_message




class MyException(Exception):
    def __init__(self, error_message:str,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details)

    def __str__(self):
        return self.error_message
