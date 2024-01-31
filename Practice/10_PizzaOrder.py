availableToppings = ['tomato','onion','garlic','ham','chicken','prmesan','chilli']
pizza = {}

#appending elements
pizza['crust'] = input('How would you like the crust, thick or thin?')
pizza['selectedToppings'] = []

topping = None
while (topping != 'end'):
    topping = input('What shall we put on your pizza?')
    pizza['selectedToppings'].append(topping)

print("Your ordered your pizza with "+str(pizza['crust']))
print("Also with the following toppings: ")
for topping in pizza['selectedToppings']:
    print(str(topping))
