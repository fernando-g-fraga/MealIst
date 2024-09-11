from handler.gemini import CreateRecipe
from handler import todoist
from app_middlewere import splitResponse

def coletaReceitas()->list[str]:
    recipe_list = []
    
    print("Bem vindo! Este aplicativo foi feito para gerar uma lista de compras com base nas receitas solicitadas.")
    

    for i in range(1,4):
        user_input = input(f"Por favor, insira abaixo o nome da receita que gostaria de agendar. Case deseje encerrar digite 0 \n")
        if  user_input ==  "0":
            break
        recipe_list.append(user_input)
        print(f"Receita {user_input} adicionada com sucesso. {i}/5")
    return recipe_list

recipe_list = coletaReceitas()
weekRecipe = splitResponse(CreateRecipe(recipe_list))
grocery_list = todoist.postGroceryListTask(weekRecipe.Grocery)
weekly_meal = todoist.postWeeklyMealTasks(weekRecipe.Recipe)