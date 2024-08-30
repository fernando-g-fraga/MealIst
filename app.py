from hadler.gemini import CreateRecipe
import json
import io


list_ingredients = []

def coletaReceitas():
    print("Bem vindo! Este aplicativo foi feito para gerar uma lista de compras com base nas receitas solicitadas.")
    
    keep_going = True
    max = 5
    count = 0
    while keep_going == True:
        ingredient = str(input(f"Digite o nome da receita ({count}/{max}). Precione enter para adicionar uma nova receita ou 0 caso tenha concluído.\n"))
        if ingredient == str(0) or count == max:
            keep_going = False
            break
        list_ingredients.append(ingredient)
        count+=1

    return list_ingredients 


output = CreateRecipe(coletaReceitas())

if output == False:
    print("Houve um erro ao gerar as receitas, tente novamente.")
    coletaReceitas()

print(output)
