from handler.gemini import CreateRecipe
from app_middlewere import ConvertToDict
import json
import io


list_ingredients = ["Macarrão Carbonara", "Pão de Queijo"]

def coletaReceitas():
    print("Bem vindo! Este aplicativo foi feito para gerar uma lista de compras com base nas receitas solicitadas.")
    
    # keep_going = True
    # max = 5
    # count = 0
    # while keep_going == True:
    #     ingredient = str(input(f"Digite o nome da receita ({count}/{max}). Precione enter para adicionar uma nova receita ou 0 caso tenha concluído.\n"))
    #     if ingredient == str(0) or count == max:
    #         keep_going = False
    #         break
    #     list_ingredients.append(ingredient)
    #     count+=1

    return list_ingredients 

list_ingredients = coletaReceitas()
gemini_response = CreateRecipe(list_ingredients)
ConvertToDict(gemini_response)


