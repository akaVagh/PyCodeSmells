import logging
from logging.handlers import RotatingFileHandler


def setup_logging(log_file='app.log', level=logging.INFO, max_size=10485760, backup_count=3):
    """Setup logging configuration."""
    handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s', '%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(level)
    logger.addHandler(handler)
