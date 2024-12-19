import logging
import os
from datetime import datetime

# Generate the log file directory based on the current date
log_dir = datetime.now().strftime("%Y-%m-%d")
log_folder = os.path.join(os.getcwd(), "logs", log_dir)

# Create a unique log file name using the current time
log_file_name = f"{datetime.now().strftime('%H-%M-%S')}.log"
log_file_path = os.path.join(log_folder, log_file_name)

# Ensure the log directory exists
os.makedirs(log_folder, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='[%(asctime)s] --- %(lineno)d - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Log a sample message to confirm logging is working
logging.info("Logging system initialized successfully.")
