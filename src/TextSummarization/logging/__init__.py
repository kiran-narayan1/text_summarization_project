import os
import sys
import logging
from datetime import datetime

LOG_FILE_DIR = f"{datetime.now().strftime('%d_%m_%y')}"
LOG_FILENAME = f"{datetime.now().strftime('%d_%m_%y_%H_%M')}.log"

LOG_FILE_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE_DIR)

os.makedirs(LOG_FILE_PATH, exist_ok=True)

LOG_FILE = os.path.join(LOG_FILE_PATH, LOG_FILENAME)
logging_str = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"

logging.basicConfig(
    
    format=logging_str,
    level=logging.INFO,
     handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")


