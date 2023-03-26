from environs import Env

environments = Env()
environments.read_env()


class Config:
    BOT_TOKEN = environments.str('TOKEN')
    PROJECT_LOG_LEVEL = environments.str('LOG_LEVEL', 'INFO')  # INFO by default
