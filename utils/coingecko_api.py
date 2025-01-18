import requests

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'ids': 'bitcoin,ethereum,solana',
        'order': 'market_cap_desc',
        'per_page': 3,
        'page': 1,
        'sparkline': 'false'
    }
    response = requests.get(url, params=params)
    return response.json()
