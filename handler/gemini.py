import google.generativeai as genIA
import os
import json
from typing import List, Dict, Any

def configureGemini():
    genIA.configure(
        api_key=os.getenv("GOOGLE_API_KEY"),
    )

    config = genIA.GenerationConfig(
        candidate_count=1,
        temperature=0.7,
        response_mime_type="application/json"
    )

    system_instruction = '''You will receive at least one recipe name and maximum 5 recipes names. 
    Your goal is to create one json file with an object list for each recipe and a separeted json for grocery shop items: 
    
    Response RECIPE JSON EXAMPLE:
    Recipes: {[
    "name": recipe name, 
    "ingredients": ["ingredient1", "ingredient2", ...], 
    "directions": ["step 1 - ..."]
    },
    "name": recipe name, 
    "ingredients": ["ingredient1", "ingredient2", ...], 
    "directions": ["step 1 - ..."]},
    ]
   
    Response GROCERY SHOP JSON EXAMPLE:
    "Grocery_shop": {"ingredient1": 2 boxes, "ingredient2": 1kg}.

    ADITIONAL INSTRUCTIONS:
    All the responses should be in portuguese.
    The Grocery_shop ingredients quantity should be increased with the recipes requirement.
    Use double-quotes everytime.
    Never accept more than 5 recipes
    '''


    model = genIA.GenerativeModel(
        "gemini-1.5-flash",
        generation_config=config,
        system_instruction=system_instruction)

    return model

def CreateRecipe(list_ingredients:list[str]):
    model = configureGemini()

    prompt = f"Give me the recipe for {list_ingredients} and the grocery list"

    response = model.generate_content(prompt)
    

    return response