import google.generativeai as genIA
import os
import typing_extensions as typing
from classes import Response_Recipe

class Recipe(typing.TypedDict):
    recipe_name: str
    ingredients: list[str]
    directions: list[str]

class Grocery(typing.TypedDict):
    ingredient: list[str]

config_Recipe = genIA.GenerationConfig(
        candidate_count=1,
        temperature=0.3,
        response_mime_type="application/json", 
        response_schema=list[Recipe]
    )

config_Grocery = genIA.GenerationConfig(
    candidate_count=1,
    temperature=0.3,
    response_mime_type="application/json", 
    response_schema=Grocery
    )

def configureGemini():
    genIA.configure(
        api_key=os.getenv("GOOGLE_API_KEY"),
    )


    system_instruction =   '''All the responses should be in portuguese.
    The Grocery_shop ingredients quantity should be increased with the recipes requirement.
    Use double-quotes everytime.
    Never accept more than 5 recipes.
    '''
    # 
    # '''You will receive at least one recipe name and maximum 5 recipes names. 
    # Your goal is to create one json file with an object list for each recipe and a separeted json for grocery shop items: 
    
    # Response RECIPE JSON EXAMPLE:
    # Recipes: {[
    # "name": recipe name, 
    # "ingredients": ["ingredient1", "ingredient2", ...], 
    # "directions": ["step  
    # "ingredients": ["ingredient1", "ingredient2", ...], 
    # "directions": ["step 1 - ..."]},
    # ]
   
    # Response GROCERY SHOP JSON EXAMPLE:
    # "Grocery_shop": {"ingredient1": 2 boxes, "ingredient2": 1kg}.

    # ADITIONAL INSTRUCTIONS:
  


    model = genIA.GenerativeModel(
        "gemini-1.5-flash",
        system_instruction=system_instruction)

    return model

def CreateRecipe(list_ingredients:list[str])-> Response_Recipe:
    model = configureGemini()
    response_recipe = Response_Recipe()
        

    recipes_prompt = f"Give me the recipe for {list_ingredients}"
    recipes_output = model.generate_content(recipes_prompt,generation_config=config_Recipe)
    response_recipe.Recipe = recipes_output.text

    grocery_prompt = f"Create a grocery shop list for those recipes {recipes_output.text}"
    grocery_ouput = model.generate_content(grocery_prompt,generation_config=config_Grocery).text
    response_recipe.Grocery = grocery_ouput
    
    return response_recipe




