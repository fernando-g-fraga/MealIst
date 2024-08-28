import google.generativeai as genIA
import os
import typing_extensions as typing
import json

genIA.configure(
    api_key=os.getenv("GOOGLE_API_KEY"),
)

class Recipe (typing.TypedDict):
    recipe_name : str
    ingredients: str




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

system_instruction = f" Your goal is to generate recipes.\
You will receive a list of ingredients available and optionally dietary restrictions\
You will output a Json format, here is a sample: {str(output_sample)}\
You will always output in portuguese Brazilian Language and use the SI Metric System"


model = genIA.GenerativeModel(
    "gemini-1.5-flash",
    generation_config=config,
    system_instruction=system_instruction)

def CreateRecipe(prompt):
    response = model.generate_content(
        contents=prompt,
        generation_config=config)

    response_str = str(response.text)


    return response_str