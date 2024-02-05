import requests
item = "mirage_prime_systems"
platform = 'pc'
response = requests.get(f'https://api.warframe.market/v1/items/{item}/orders?include=item')

#check to see if the request was successful

if response.status_code == 200:
    data = response.json()
    orders = data['payload']['orders']
    sell_orders = []
    sell_orders_string = set()
    for order in orders:
        
        if order['order_type'] == 'sell' and order['platform'] =='pc' and order['user']['status'] == 'ingame':
            order_string = f"{order['user']['ingame_name']}-{order['platinum']}"
            if order_string not in sell_orders_string:
                sell_orders.append({'user': order['user']['ingame_name'], 'price': float(order['platinum'])})
                sell_orders_string.add(order_string)
    sorted_sell_orders = sorted(sell_orders, key=lambda k: k['price'])
        
    for order in sorted_sell_orders:
        print(f"User: {order['user']}, Price: {order['price']}")
else:
    print(f"failed, status code: {response.status_code}")