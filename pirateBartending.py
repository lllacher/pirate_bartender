import random

def get_drink_preference():
    """ This function determines what the drink preferences are of the customer."""
    questions = {
        "strong": "Do ye like yer drinks strong?",
        "salty": "Do ye like it with a salty tang?",
        "bitter": "Are ye a lubber who likes it bitter?",
        "sweet": "Would ye like a bit of sweetness with yer poison?",
        "fruity": "Are ye one for a fruity finish?",
    }
    responses = {}
    print("Welcome to the Pirate Bar! I wonder what type of drink you would like?")
    print("I'll ask ye a bunch of questions and ye need to answer either Yay or Nay.")
    for k, v in questions.items():
        answer = input(v+" ")
        if (answer == "Yay") or (answer == "Nay"):
            responses[k] = answer
        else:
            print("Seeing as how ye don't know how to answer properly, I guess it'll be Nay!!!")
            responses[k] = "Nay"
    return responses
        
def make_drink(preference):
    """ This function collects all the ingredients for the drink based on the preferences passed into the function."""
    ingredients = {
        "strong": ["glug of rum", "slug of whisky", "splash of gin"],
        "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
        "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
        "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
        "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
    }
    drink = []
    for k, v in preference.items():
        if v == "Yay":
            drink.append(random.choice(ingredients[k]))
    return drink

if __name__ == '__main__':
    customers_preferences = get_drink_preference()
    drink = make_drink(customers_preferences)
    if drink == []: # there are no ingredients
        print("\nYe must be a teetotaler, so here's your water!")
    else:
        s = ", "
        print("\nI'll mix a {} to make yer poison!".format(s.join(drink)))
