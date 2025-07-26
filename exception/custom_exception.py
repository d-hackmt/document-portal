import sys
import traceback
from logger.custom_logger import CustomLogger  # Custom logger class

# Initialize logger for this file
logger = CustomLogger().get_logger(__file__)

# Custom exception class for structured error reporting
class DocumentPortalException(Exception):
    """Custom exception for Document Portal"""

    def __init__(self, error_message, error_details: sys):
        # Extract traceback info from sys.exc_info()
        _, _, exc_tb = error_details.exc_info()

        # Get filename and line number where exception occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.lineno = exc_tb.tb_lineno

        # Store the original error message
        self.error_message = str(error_message)

        # Format the full traceback as a string
        self.traceback_str = ''.join(traceback.format_exception(*error_details.exc_info())) 

    def __str__(self):
        # Define the custom string representation of the exception
        return f"""
        Error in [{self.file_name}] at line [{self.lineno}]
        Message: {self.error_message}
        Traceback:
        {self.traceback_str}
        """

# Testing the custom exception handling
if __name__ == "__main__":
    try:
        # Simulate an error (division by zero)
        a = 1 / 0
        print(a)

    except Exception as e:
        # Raise and log the custom exception
        app_exc = DocumentPortalException(e, sys)
        logger.error(app_exc)
        raise app_exc
