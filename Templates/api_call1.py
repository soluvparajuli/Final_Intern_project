import requests
from config import config

def api_call1(name_the_ingredient):
    payload = {
        'ingredients':name_the_ingredient,
        'number': 2,
        # can be changed according to required number of receipe we are getting only 2 receipe for now
        'ranking': 1  # ranking is done by system , I am unknown about the ranking
    }
    endpoint = "https://api.spoonacular.com/recipes/findByIngredients"
    headers = {
        'x-api-key': config.api_key
    }
    try:
        observation = requests.get(endpoint, params=payload, headers=headers)
        observation = observation.json()
        if len(observation) > 0:
            print("run api completed")
            return observation
        else:
            # print("run completed but failed")
            pass
    except:
        print("Provide ingredient is not in our any receipe")
