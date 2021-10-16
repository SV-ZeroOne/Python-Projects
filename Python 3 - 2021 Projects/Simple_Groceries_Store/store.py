"""
Simple Groceries
"""
import store_service


items_to_purchase = {
    'candy': 7,
    'notebook': 15,
    'paper': 8,
    'coffee': 3,
    'socks': 7
}

def application_start():
    # Check to see if user enters in proper numeric money value instead of some string
    user_money_real = False
    while not user_money_real:
        user_money = input('How much money do you have? ')
        if user_money.isdigit():
            user_money = int(user_money)
            user_money_real = True


    items_price_added_to_cart = []

    user_shopping = False

    while not user_shopping:
        add_item_to_cart = input('What item would you like to add to your cart? ')
        # Check if key exists
        if add_item_to_cart.lower() in items_to_purchase:
            items_price_added_to_cart.append(items_to_purchase.get(add_item_to_cart))
            print(f'You currently have {len(items_price_added_to_cart)} items in your cart.')
        else:
            print('Item is not available at this store')
            continue

        keep_shopping = input('Do you wish to continue shopping? (Y = yes, N = no) ')
        if keep_shopping.lower().strip() == 'n':
            user_shopping = True

    store_service.purchase_items(user_money, items_price_added_to_cart)


application_start()