from  .hadler import gemini
from  .hadler import todoist
from app import list_ingredients,CreateRecipe,coletaReceitas

def convertToDict (gemini_reponse: str) -> dict:
    respose_json = eval(gemini_reponse)
    return respose_json

def splitGrocery (respose_json :dict) -> dict:
    grocery_list = dict(respose_json.get("Grocery_shop"))

    return grocery_list

gemini_reponse = CreateRecipe(list_ingredients)

if gemini_reponse == False:
    print("Houve um erro ao gerar as receitas, tente novamente.")
    coletaReceitas()

for index in gemini_reponse:
    recipe = convertToDict(gemini_reponse[index])
    grocery_list = splitGrocery(recipe)
    