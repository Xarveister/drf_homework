from django.contrib.sites import requests
from django.shortcuts import redirect

from config.settings import STRIPE_SECRET_KEY


def create_checkout_session(product, price):

    url = 'https://api.stripe.com/v1/checkout/sessions'

    headers = {'Authorization': f'Bearer {STRIPE_SECRET_KEY}'}
    data = {
        'product': product,
        'price': price
    }
    response = requests.post(url, headers, data)
    if response.status_code != 200:
        raise Exception(f"Ошибка получения данных {response.status_code}")
    data_checkout_session = response.json()

    return redirect(data_checkout_session.url)