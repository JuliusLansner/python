import requests
item = "mirage_prime_systems_blueprint"
platform = 'pc'
response = requests.get(f'https://api.warframe.market/v1/{platform}/items/{item}/orders')

#check to see if the request was successful
if response.status_code == 200:
    data = response.json()
    orders = data['payload']['order']
    for order in orders:
        if order['order_type'] == 'sell':
            print(f"User: {order['user']['ingame_name']}, Price: {order['Platinum:']}")
        
    
else:
    print(f"failed, status code: {response.status_code}")
    
