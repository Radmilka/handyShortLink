import requests


def shorten_url(url):
    response = requests.get('https://clck.ru/--', params={'url': url})
    short_url = response.content.decode('utf-8')
    return short_url
