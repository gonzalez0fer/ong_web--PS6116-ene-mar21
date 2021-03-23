import requests

def get_exchange_rate():
    r = requests.get('https://s3.amazonaws.com/dolartoday/data.json')
    return r.json()['USD']['sicad2']