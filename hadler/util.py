data = ['{"Recipes": {"name": "Macarrão Carbonara", "ingredients": ["500g de espaguete", "200g de pancetta cortada em cubos", "2 ovos grandes", "2 gemas", "50g de queijo parmesão ralado", "2 colheres de sopa de água de cozimento do macarrão", "Pimenta do reino moída na hora", "Sal"], "directions": ["Cozinhe o espaguete em água fervente com sal até ficar al dente.", "Enquanto o macarrão cozinha, doure a pancetta em uma panela grande em fogo médio até ficar crocante.", "Retire a pancetta da panela e reserve.", "Em uma tigela grande, bata os ovos, as gemas, o queijo parmesão, a água de cozimento do macarrão e a pimenta do reino até obter um creme homogêneo.", "Escorra o macarrão e adicione-o à panela com a pancetta.", "Mexa bem para combinar.", "Adicione o creme de ovos à panela com o macarrão e a pancetta e mexa vigorosamente até que o molho engrosse.", "Sirva imediatamente, decorado com queijo parmesão ralado."] }, "Grocery_shop": {"espaguete": "1 pacote", "pancetta": "200g", "ovos": "4 unidades", "queijo parmesão": "50g", "pimenta do reino": "1 pote"}}\n', '{"Recipes": {"name": "Sopa de Abóbora", "ingredients": ["1 kg de abóbora em cubos", "1 cebola picada", "2 dentes de alho picados", "1 colher de sopa de azeite extra virgem", "1 litro de caldo de legumes", "Sal e pimenta do reino a gosto", "1/2 xícara de salsinha picada", "1/4 xícara de creme de leite fresco"], "directions": ["Em uma panela grande, aqueça o azeite em fogo médio.", "Adicione a cebola e o alho picados e refogue até ficarem macios.", "Acrescente a abóbora em cubos e refogue por mais 5 minutos.", "Despeje o caldo de legumes, tempere com sal e pimenta do reino a gosto e cozinhe em fogo baixo por cerca de 20 minutos, ou até a abóbora ficar macia.", "Transfira a sopa para um liquidificador e bata até obter um creme homogêneo.", "Retorne a sopa para a panela e adicione a salsinha picada.", "Sirva quente, decorado com uma colher de sopa de creme de leite fresco."] }, "Grocery_shop": {"abóbora": "1 kg", "cebola": "1", "alho": "2 dentes", "azeite extra virgem": "1 colher de sopa", "caldo de legumes": "1 litro", "sal": "a gosto", "pimenta do reino": "a gosto", "salsinha": "1/2 xícara", "creme de leite fresco": "1/4 xícara"}}\n']

def convertToDict (prompt_listed: str) -> dict:
    dict1 = eval(prompt_listed)
    return dict1

recipe = convertToDict(data[0])

def splitGrocery (full_prompt :dict) -> dict:
    grocery_list = dict(full_prompt.get("Grocery_shop"))

    return grocery_list

grocery = splitGrocery(recipe)
print("priting Recipe:")
print(recipe["Recipes"])
print("priting Grocery:")
print(grocery)

