from hadler.gemini import CreateRecipe
import json
import io

list_ingredients = []

print("Bem vindo! Para iniciarmos, digite abaixo quais ingredientes você possui disponível.")

keep_going = True
max = 5
count = 0
# while keep_going == True:
#     ingredient = input(f"Digite um ingrediente ({count}/{max}) e pressione enter para seguir ou 0 para sair.\n")
#     if ingredient == str(0) or count == max:
#         keep_going = False
#     list_ingredients.append(ingredient)
#     count+=1


# prompt_cooked = f"Crie uma receita com os seguintes ingredientes: {list_ingredients}"
prompt_cooked = f"Crie uma receita com os seguintes ingredientes: Macarrão e Carne Moída"

output = CreateRecipe(prompt_cooked)

print(output.replace("json","").replace("```",""))

json_data = dict(json.loads(output))




