cookbook = {
    'sandwich':{
        'ingredients':['ham','bred','cheese','tomatoes'],
        'meal':'lunch',
        'prep_time':10
    },
    'cake':{
        'ingredients':['flour','sugar','eggs'],
        'meal':'dessert',
        'prep_time':60
    },
    'salad':{
        'ingredients':['avocado','arugula','tomatoes','spinach'],
        'meal':'lunch',
        'prep_time':15
    }
}

def print_recipe(name):
    try:
        meal = cookbook[name]
    except:
        print(f"The recipe ({name}) does not exist in the cookbook")
    else:
        print('Recipe for',name)
        print('Ingredients list:',meal['ingredients'])
        print('To be eaten for',meal['meal'])
        print(f"Takes {meal['prep_time']} minutes of cooking")

def del_recipe(name):
    try:
        del cookbook[name]
    except:
        print(f"The recipe ({name}) does not exist in the cookbook")

def add_recipe(name:str, ingredients:list[str], meal:str, prep_time:int):
    cookbook[name]={
        'ingredients':ingredients,
        'meal':meal,
        'prep_time':prep_time
    }

def print_all():
    print('-'*11)
    for name in cookbook:
        print_recipe(name)
        print()
        print('-'*11)

