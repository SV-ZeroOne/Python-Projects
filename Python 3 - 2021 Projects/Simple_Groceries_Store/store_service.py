"""
Store service is used to calculate the total cost of the grocery list
and to see if user has enough money
"""

def purchase_items(user_money, items):
    items_total_cost = 0
    for item in items:
        items_total_cost = items_total_cost + item
        
    if items_total_cost <= user_money:
        amount_left = user_money - items_total_cost
        print(f'Purchase Complete: ${amount_left} left')
    else:
        print('You cannot afford all of these items.')

# Test case
arg_1 = 15
arg_2 = [10, 2]
# purchase_items(arg_1, arg_2)