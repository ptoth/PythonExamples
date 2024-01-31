# Declaring foods and drinks
menu = {
    'cola': 350,
    'pizza': 1500,
    'burger': 1350,
}


total = 0
order = input('What can I get you?')

if order == 'cola':
    total += menu[order]

print('Total =' +str(total))

# Placing some new beverages
menu['fanta'] = 350
menu['beer'] = 200

# removing beer
del menu['beer']

order = menu.get(input('What can I get you?'),'Sorry, we do not have that as of now.')
print(str(order))

for item, price in menu.items():
    print("Item name :"+ str(item))
    print("Item price:"+ str(price))
