from  handler import gemini
from  handler import todoist
from typing import List, Dict, Any
import json

def ConvertToDict (gemini_reponse: List):
    recipes_grocery: List[Dict[str,Any]] = []
    recipes: List[Dict[str,Any]] = []
    grocery: List[Dict[str,Any]] = []

    for index in gemini_reponse:
        dict_convert = dict(json.loads(index))
        recipes_grocery.append(dict_convert)
    
    for item in recipes_grocery:
        if item.get() 

                      

# gemini_reponse = CreateRecipe(list_ingredients)

# if gemini_reponse == False:
#     print("Houve um erro ao gerar as receitas, tente novamente.")
#     coletaReceitas()

# for index in gemini_reponse:
#     recipe = convertToDict(gemini_reponse[index])
#     grocery_list = splitGrocery(recipe)
