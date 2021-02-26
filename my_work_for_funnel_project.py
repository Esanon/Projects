import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visits_carts = pd.merge(visits, cart, how='left')

print(visits_carts)

visits_carts_rows = len(visits_carts)

print(visits_carts_rows)

null_carts = len(visits_carts[visits_carts.cart_time.isnull()])
print(null_carts)

print(float(null_carts)/(visits_carts_rows))

checkout_cart = pd.merge(cart,checkout,how='left')
print(checkout_cart)

checkout_number = len(checkout_cart)
print(checkout_number)

null_checkout = len(checkout_cart[checkout_cart.checkout_time.isnull()])
print(null_checkout)

print(float(null_checkout)/(checkout_number))

all_data = visits.merge(cart, how='left').merge(checkout, how = 'left').merge(purchase, how = 'left')
print(all_data.head())

checkout_purchase = pd.merge(checkout, purchase, how='left')
print(checkout_purchase.head())

purchase_number = len(checkout_purchase)
print(checkout_purchase)

null_purchase = len(checkout_purchase[checkout_purchase.purchase_time.isnull()])
print(null_purchase)

print(float(null_purchase)/purchase_number)

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
print(all_data.head())
print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())