import logging
from config import Config
from bot_methods import start


if __name__ == '__main__':
    logging.basicConfig(level=Config.PROJECT_LOG_LEVEL)  # Уровень логирования
    start()
