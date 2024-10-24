import logging
import os

def setup_logger(file_name, log_file):
    """Функция настройки логов для модулей"""

    os.makedirs("logs", exist_ok = True)
    logger = logging.getLogger(file_name)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file, mode="w")
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(Levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    return logger