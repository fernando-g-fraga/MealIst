from hadler.gemini import CreateRecipe
import json
import io

list_ingredients = []

print("Bem vindo! Este aplicativo foi feito para gerar uma lista de compras com base nas receitas solicitadas.")

keep_going = True
max = 5
count = 0
while keep_going == True:
    ingredient = input(f"Digite o nome da receita ({count}/{max}). Precione enter para adicionar uma nova receita ou 0 caso tenha concluído.\n")
    if ingredient == str(0) or count == max:
        keep_going = False
    list_ingredients.append(ingredient)
    count+=1


prompt_cooked = f"Crie uma receita com os seguintes ingredientes: {list_ingredients}"

output = CreateRecipe(prompt_cooked)

print(output.replace("json","").replace("```",""))

json_data = dict(json.loads(output))




