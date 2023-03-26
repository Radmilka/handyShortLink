import logging

import requests


def is_link_ok(message):
    try:
        response = requests.get(message)
        response.raise_for_status()
        return response.ok
    except Exception as e:
        logging.log(level=logging.INFO, msg=f"Ошибка при введении ссылки: {e}")
        return False
    