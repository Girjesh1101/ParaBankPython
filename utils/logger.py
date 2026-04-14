import datetime
import logging
import os

timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
log_dic = "logs"
os.makedirs(log_dic, exist_ok=True)
log_file = os.path.join(log_dic, f"test_{timestamp}.log")

def get_logger(name):

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
