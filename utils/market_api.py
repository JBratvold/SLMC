# esiAPI.py

import requests
from config import JITA_SYSTEM_ID

def get_market_price(type_id):
    """Fetches the lowest Jita market price for a material."""
    url = f'https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id={type_id}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        orders = response.json()

        # Find the cheapest price in Jita
        jita_orders = [order for order in orders if order['system_id'] == JITA_SYSTEM_ID]
        return min((order['price'] for order in jita_orders), default=None)

    except requests.exceptions.RequestException:
        return None  # If API fails, return None
