import logging

import requests


def shorten_url(url):
    try:
        response = requests.get('https://clck.ru/--', params={'url': url})
        response.raise_for_status()
        short_url = response.content.decode('utf-8')
        return short_url
    except Exception as e:
        logging.log(level=logging.ERROR, msg=e)
        return "Произошла ошибка. Попробуйте еще раз позже"
