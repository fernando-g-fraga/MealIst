import datetime

def get_WeekArray(recipe_list:dict)-> list[str]:
    week_Days = []
    
    start_date = datetime.datetime.now()
    end =  len(recipe_list) + start_date.day

    for i in range(start_date.day,end):
            x = datetime.date(start_date.year,start_date.month,i)    
            week_Days.append(x.strftime("%A"))
            
    return week_Days

respose_example_recipes = {"Macarrão Carbonara": {"name": "Macarrão Carbonara", "ingredients": ["500g de macarrão espaguete", "200g de pancetta em cubos", "2 ovos grandes", "50g de queijo parmesão ralado", "2 colheres de sopa de água da massa", "Sal e pimenta do reino a gosto"], "directions": ["Cozinhe o macarrão em água fervente com sal até ficar al dente.", "Enquanto o macarrão cozinha, frite a pancetta em uma panela até ficar crocante.", "Bata os ovos com o queijo parmesão e a água da massa até obter um creme homogêneo.", "Escorra o macarrão e adicione-o à panela com a pancetta.", "Despeje o creme de ovos e queijo sobre o macarrão e misture bem.", "Tempere com sal e pimenta do reino a gosto.", "Sirva imediatamente."] }, "Pão de Queijo": {"name": "Pão de Queijo", "ingredients": ["1 xícara (240ml) de leite integral", "1 xícara (120g) de polvilho doce", "1 xícara (120g) de polvilho azedo", "1 colher de sopa (15g) de manteiga", "1 ovo grande", "1/2 colher de chá (3g) de sal", "1/2 xícara (100g) de queijo minas padrão ralado"], "directions": ["Misture o leite, o polvilho doce, o polvilho azedo, a manteiga, o ovo, o sal e o queijo em uma tigela.", "Amasse bem com as mãos até obter uma massa lisa e homogênea.", "Pré-aqueça o forno a 200°C.", "Unte uma forma com manteiga e farinha.", "Faça bolinhas com a massa e coloque-as na forma.", "Asse por 20 minutos ou até dourar."] }}
get_WeekArray(respose_example_recipes)