import _collections
from collections import Counter

# def display(diff):
game=True
resource = {
    'milk': 2000,
    'water': 5000,
    'coffee': 200
}

latte = {
    'milk': 150,
    'water': 200,
    'coffee': 24,
}

capucino={'milk':100,'water':250,
          'coffee': 24}
espreso={
    'water':50,
    'coffee':18
}

def buylatte(choice):
        resource = {
            'milk': 2000,
            'water': 5000,
            'coffee': 200
        }
        if choice == "latte":
            recipe = latte
        elif choice == "capucino":
            recipe = capucino
        elif choice in ("espreso","espresso"):
            recipe = espreso
        else:
            print("Invalid choice. Please select latte, capucino, or espreso.")
            return

        temp1 = Counter(resource)
        temp2 = Counter(recipe)
        res = temp1 - temp2
        print(f"Here is your {choice}")
        print( f"Left amount is: milk= {res['milk']}, water= {res['water']}, coffe= {res['coffee']}")
        buylatte(choice)


while True:
    # Check if resources are depleted
    if resource['milk'] <= 0 or resource['water'] <= 0 or resource['coffee'] <= 0:
        print("Shop is closed.")
        break

    # Prompt the user for input
    choice = input("What would you like (latte, capucino, espreso)? ").lower()
    buylatte(choice)
