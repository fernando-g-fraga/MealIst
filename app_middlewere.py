from typing import List, Dict, Any
from classes import Response_Recipe


def splitResponse(full_response:Dict) -> Response_Recipe:
    splited_Recipe = Response_Recipe()
    splited_Recipe.Grocery = full_response.get("Grocery_shop")

    for key in full_response.keys():
        if key != "Grocery_shop":
            splited_Recipe.Recipe.append(full_response[key])        
            
    return splited_Recipe

