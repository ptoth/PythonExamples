def greet_user():
    """Display a simple greeting."""
    print("Hello!")

def greet_with_name(username):
    print ("Welcome "+username+"!")

greet_user()
greet_with_name(input("Please type your name: "))

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# calling function with incorrect order of parameters:
describe_pet('harry', 'hamster')

# calling function with explicit parameter binging, no matter the order
describe_pet(animal_type='hamster', pet_name='harry')

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# conditional parameter
def get_formatted_name_with_opt_middle_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name_with_opt_middle_name('john', 'hooker', 'lee')
print(musician)
