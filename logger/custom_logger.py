import logging
import os
from datetime import datetime

# Custom logger class to create timestamped log files
class CustomLogger:
    def __init__(self):
        self.logger = logging.getLogger("DocumentPortal")
        self.logger.setLevel(logging.INFO)

        # Create a logs directory if it doesn't exist
        self.logs_dir = os.path.join(os.getcwd(), "logs")
        os.makedirs(self.logs_dir, exist_ok=True)

        # Generate a timestamped log file name
        self.LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        self.LOG_FILE_PATH = os.path.join(self.logs_dir, self.LOG_FILE)

        # Set up logging configuration to file
        logging.basicConfig(
            filename=self.LOG_FILE_PATH,
            format="[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s",
            level=logging.INFO,
        )

    # Returns a logger instance for a given file/module
    def get_logger(self, name=__file__):
        return logging.getLogger(os.path.basename(name))


# Test the logger setup
if __name__ == "__main__":
    logger_instance = CustomLogger()
    logger = logger_instance.get_logger(__file__)
    logger.info("Custom logger is working!")
