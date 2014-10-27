# -*- encoding: utf-8 -*-

import requests


def image_search(query):
    url = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s' % (query)
    res = requests.get(url)

    if res.status_code != 200:
        return []

    result = res.json()
    return [r for r in result['responseData']['results']]


def first_image(query):
    images = image_search(query)

    if len(images) > 0:
        return images[0].get('unescapedUrl', '')
    else:
        return ''
