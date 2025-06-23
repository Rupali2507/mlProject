import sys
import logging
from src import logger
 # If you want to print/use the path, otherwise not needed

def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script: {file_name} at line number: {exc_tb.tb_lineno} error message: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)

    def __str__(self):
        return self.error_message

    def log_error(self):
        logging.error(self.error_message)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.error_message})"


