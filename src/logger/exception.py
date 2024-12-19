import sys

def get_custom_error(error, error_info: sys):
    """
    Constructs a detailed error message including the file name, line number,
    and the error message.

    Args:
        error (Exception): The exception object.
        error_info (sys): The sys module to extract exception details.

    Returns:
        str: Formatted error message.
    """
    _, _, exb = error_info.exc_info()
    line_no = exb.tb_lineno
    file_name = exb.tb_frame.f_code.co_filename
    error_message = (
        f"Error occurred in Python script: {file_name}. "
        f"Line number: {line_no}, Error message: {str(error)}"
    )
    return error_message

class CustomError(Exception):
    """
    Custom exception class that generates detailed error messages.
    """
    def __init__(self, error, error_detail: sys):
        """
        Initializes the CustomError with a detailed error message.

        Args:
            error (Exception): The exception object.
            error_detail (sys): The sys module to extract exception details.
        """
        self.error_message = get_custom_error(error, error_detail)
        super().__init__(self.error_message)

    def __str__(self):
        """
        Returns the error message as a string representation.
        """
        return self.error_message
