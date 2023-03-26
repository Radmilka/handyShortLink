import logging
from config import Config
from bot import start


if __name__ == '__main__':
    logging.basicConfig(level=Config.LOG_LEVEL.value)
    start()
