import requests
item = "mirage_prime_systems"
platform = 'pc'
response = requests.get(f'https://api.warframe.market/v1/items/{item}/orders?include=item')

#check to see if the request was successful
if response.status_code == 200:
    data = response.json()
    orders = data['payload']['orders']
    for order in orders:
        if order['order_type'] == 'sell' and order['platform'] =='pc' and order['user']['status'] == 'ingame':
            print(f"User: {order['user']['ingame_name']}, Price: {order['platinum']}")
else:
    print(f"failed, status code: {response.status_code}")