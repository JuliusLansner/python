import requests

def get_sorted_orders(item):
    item = item.replace(" ","_")
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



def get_item_set(item):
    item = item.replace(" ","_")
    
    
def main():
    choice = input("1: Price single item - 2: Price compare")
    
    if choice == "1":
        item = input("what item do you want to see the price of?\n")
        get_sorted_orders(item)
    if choice == "2":
         item = input("What set do you wantt to search for?")
         get_item_set(item)
    else:
        print("Please choose 1 or 2")
        
main()