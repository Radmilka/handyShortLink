from enum import Enum
from environs import Env

env = Env()
env.read_env()


class Config(Enum):
    TOKEN = env.str('TOKEN')
    LOG_LEVEL = env.str('LOG_LEVEL', 'INFO')
