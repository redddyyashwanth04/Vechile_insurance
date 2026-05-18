import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime
#constants for log configuration
LOG_DIR='logs'
LOG_FILE=f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
MAX_LOG_SIZE=5*1024*1024 #5MB
BACKUP_COUNT=3

#construct log file path
log_dir_path=os.path.join(from_root(),LOG_DIR)
os.makedirs(log_dir_path,exist_ok=True)
log_file_path=os.path.join(log_dir_path,LOG_FILE)

def configure_logger():
    #this is the custom logger
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)
       #formater for log messages
    formatter=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    #file handler with rotation
    file_handler=RotatingFileHandler(log_file_path,maxBytes=MAX_LOG_SIZE,backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    #console handler for output to console
    console_handler=logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    #add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

configure_logger()
#create logger
#set the format
#adding the file and console handlers to the logger
#adding the handlers to the logger



