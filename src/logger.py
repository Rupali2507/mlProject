import logging
import os
from datetime import datetime 

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Directory path for logs
logs_dir = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s %(name)s %(levelname)s %(message)s',
    level=logging.INFO,
)

def get_log_file_path():
    """
    Returns the path of the log file.
    """
    return LOG_FILE_PATH
