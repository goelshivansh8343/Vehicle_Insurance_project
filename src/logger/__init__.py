import logging
import os
from datetime import datetime
from from_root import from_root


LOG_DIR='logs'
LOG_FILE=f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
MAX_LOG_SIZE=5*1024*1024
BACKUP_COUNT=3
LOG_DIR_PATH=os.path.join(from_root(),LOG_DIR)
os.makedirs(LOG_DIR_PATH,exist_ok=True)
LOG_FILE_PATH=os.path.join(LOG_DIR_PATH,LOG_FILE)


def configure_logger():
    logger=logging.getLogger()
    logger.setLevel("DEBUG")

    formatter=logging.Formatter("[%(asctime)s - %(name)s - %(levelname)s - %(message)s]")
    # Console hanfdler
    file_handler=logging.FileHandler(LOG_FILE_PATH)
    file_handler.setLevel("DEBUG")
    console_handler=logging.StreamHandler()
    console_handler.setLevel("DEBUG")


    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)



configure_logger()