from handler.util import response_example
from typing import List, Dict, Any
import json

class Response_Recipe:
    def __init__(self) -> None:
        self.Recipe: List[Dict[str,str]] = []
        self.Grocery: Dict[str,Any] = []

def splitResponse(full_response:Dict) -> Response_Recipe:
    splited_Recipe = Response_Recipe()
    splited_Recipe.Grocery.append(full_response.get("Grocery_shop"))

    for key in full_response.keys():
        if key != "Grocery_shop":
            splited_Recipe.Recipe.append(full_response[key])        
            
    return splited_Recipe