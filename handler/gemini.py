import google.generativeai as genIA
import os

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

    system_instruction = '''You will receive at least a recipe. Your goal is to create two json files: 
                        Recipes: {
                        name: recipe name, 
                        ingredients: ["ingredient1", "ingredient2", ...], 
                        directions: ["step 1 - ..."]} 
                        Grocery_shop: {"ingredient1": 2 boxes, "ingredient2": 1kg}. 
                        All the responses should be in portuguese'''


    model = genIA.GenerativeModel(
        "gemini-1.5-flash",
        generation_config=config,
        system_instruction=system_instruction)

    return model

def CreateRecipe(list_ingredients:list):
    model = configureGemini()
    recipe = []
    for i in list_ingredients:
        prompt = f"Give me the recipe for {i} and the grocery list"
        try: 
            recipe.append(model.generate_content(contents=prompt).text)
        except:
            return False
        
    return recipe