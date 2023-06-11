import logging
import os
from datetime import datetime
from from_root import from_root

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}"

log_file_path = os.path.join(from_root(), 'logs', LOG_FILE)

os.makedirs(log_file_path, exist_ok=True)

log_file_name = os.path.join(log_file_path, LOG_FILE)

logging.info(
    filename=log_file_name,
    format= "[%(asctime)] %(name)s - %(levelname)s - %(message)s",
    level = logging.info()
)