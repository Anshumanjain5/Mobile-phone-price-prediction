import logging 
import os
from datetime import datetime

file_dir = datetime.now().strftime("%Y-%m-%d")
file_folder = os.path.join(os.getcwd,"logs",file_dir)
file_name = f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.log"
file_path = os.path.join(file_folder,file_name)
os.makedirs(file_folder,exist_ok=True)

logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format='[%(asctime)s] --- %(lineno)d - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)