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

    output_sample =   {"recipe": {
            "name": "Recipe Name",
            "ingredients": [
                "First Ingredient",
                "Second Ingredient",
                "..."
            ],
            "instructions": [
                "Preheat oven to 400 degrees F (200 degrees C)....",
            ]}
        }

    system_instruction = '''You will receive at least one recipe. Your goal is to create one json file for each recipe and only one grocery shop json: 
                        Recipes: {
                        name: recipe name, 
                        ingredients: ["ingredient1", "ingredient2", ...], 
                        directions: ["step 1 - ..."]} 
                        Grocery_shop: {"ingredient1": 2 boxes, "ingredient2": 1kg}. 
                        All the responses should be in portuguese
                        The Grocery_shop ingredients quantity should be increased with the recipes requirement.
                         '''


    model = genIA.GenerativeModel(
        "gemini-1.5-flash",
        generation_config=config,
        system_instruction=system_instruction)

    return model

def CreateRecipe(list_ingredients:list[str]) -> dict:
    model = configureGemini()
    full_response:Dict
    prompt = f"Give me the recipe for {list_ingredients} and the grocery list"
    full_responseText = model.generate_content(prompt).text
    print(full_responseText)
    full_response = json.loads(full_responseText)


    return full_response