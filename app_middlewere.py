from typing import List, Dict, Any
from classes import Response_Recipe
from json import loads

def splitResponse(full_response) -> Response_Recipe:
    splited_Recipe = Response_Recipe()
    parser_ToDict:dict = loads(full_response)

    splited_Recipe.Grocery = parser_ToDict.get("Grocery_shop")
    splited_Recipe.Recipe = parser_ToDict.get("Recipes")

    return splited_Recipe 
