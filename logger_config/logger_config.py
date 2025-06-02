import os
import logging
from logging import Logger
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

# Environment config
ENV = os.getenv("ENV", "production").lower()
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
IS_DEV = ENV == "development"

LEVEL_MAP = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}
DEFAULT_LEVEL = LEVEL_MAP.get(LOG_LEVEL, logging.INFO)

def setup_logger(
    name: str,
    log_file: str,
    level: int = DEFAULT_LEVEL,
    to_console: bool | None = None
) -> Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.hasHandlers():
        logger.handlers.clear()

    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)  # <--- ensure correct log level
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s\n%(message)s\n"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # Console handler
    if to_console is True or (to_console is None and IS_DEV):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)  # <--- ensure correct log level
        console_formatter = logging.Formatter(
            "%(name)s - %(levelname)s\n%(message)s\n\n"
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    return logger
