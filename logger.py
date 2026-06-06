"""
logger.py

EEG Desktop Automation Logging System
"""

import logging
import os
from logging.handlers import TimedRotatingFileHandler

# Create logs directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "command_log.txt")

# Create logger
logger = logging.getLogger("EEGAutomation")

if not logger.handlers:

    logger.setLevel(logging.INFO)

    # File Handler
    file_handler = TimedRotatingFileHandler(
        LOG_FILE,
        when="midnight",
        interval=1,
        backupCount=7,
        encoding="utf-8"
    )

    # Console Handler
    console_handler = logging.StreamHandler()

    # Format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(module)s | %(funcName)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.propagate = False


def log_command(command):
    logger.info(f"COMMAND: {command}")


def log_signal(signal_value):
    logger.info(f"EEG SIGNAL: {signal_value}")


def log_mqtt(message):
    logger.info(f"MQTT: {message}")


def log_warning(message):
    logger.warning(message)


def log_error(message):
    logger.error(message)


def log_system(message):
    logger.info(f"SYSTEM: {message}")


logger.info("EEG Desktop Automation Logging Initialized")