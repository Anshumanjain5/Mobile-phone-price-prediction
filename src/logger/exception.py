import sys
from logger import logging

def get_custom_error(error, error_info: sys):
    _, _, exb = error_info.exc_info()
    line_no = exb.tb_lineno
    file_name = exb.tb_frame.f_code.co_filename
    error_message = (
        f"Error occurred in Python script: {file_name}. "
        f"Line number: {line_no}, Error message: {str(error)}"
    )
    logging.error(error_message)
    return error_message

class CustomError(Exception):
    def __init__(self, error, error_detail: sys):
        self.error_message = get_custom_error(error, error_detail)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message
    
