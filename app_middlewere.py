from typing import List, Dict, Any
from classes import Response_Recipe
from json import loads

def splitResponse(full_response) -> Response_Recipe:
    splited_Recipe = Response_Recipe()
    parser_ToDict:dict = loads(full_response)

    splited_Recipe.Grocery = parser_ToDict.get("Grocery_shop")
    splited_Recipe.Recipe = parser_ToDict.get("Recipes")

    return splited_Recipe 


response = '''{"Recipes": [{"name": "Macarrão Carbonara", "ingredients": ["500g de macarrão espaguete", "200g de pancetta em cubos", "3 ovos grandes", "50g de queijo parmesão ralado", "1/2 xícara de água do cozimento do macarrão", "Sal e pimenta do reino a gosto"], "directions": ["Cozinhe o macarrão em água fervente com sal até ficar al dente.", "Enquanto o macarrão cozinha, frite a pancetta em uma panela até ficar crocante.", "Bata os ovos, o queijo parmesão e a água do cozimento do macarrão em um bowl até obter um creme homogêneo.", "Escorra o macarrão e adicione-o à panela com a pancetta.", "Misture o creme de ovos com o macarrão e a pancetta.", "Tempere com sal e pimenta do reino a gosto.", "Sirva imediatamente."] }, {"name": "Pão de Queijo", "ingredients": ["1 xícara (240ml) de leite integral", "1/2 xícara (120ml) de óleo vegetal", "1 ovo grande", "1 colher de sopa (15g) de queijo parmesão ralado", "1 colher de sopa (15g) de manteiga sem sal", "1 colher de chá (5g) de sal", "2 xícaras (280g) de polvilho doce", "1/2 xícara (60g) de queijo minas padrão ralado"], "directions": ["Em uma panela média, misture o leite, o óleo, o ovo, o queijo parmesão, a manteiga e o sal.", "Leve ao fogo médio, mexendo sempre, até ferver.", "Retire do fogo e adicione o polvilho doce, mexendo até obter uma massa homogênea.", "Adicione o queijo minas padrão ralado e misture bem.", "Com as mãos untadas com óleo, modele bolinhas de massa do tamanho de uma noz.", "Acomode as bolinhas em uma assadeira untada e enfarinhada.", "Asse em forno pré-aquecido a 180°C por 30 minutos ou até dourar."] }], "Grocery_shop": {"macarrão espaguete": "1 pacote", "pancetta": "200g", "ovos": "6 unidades", "queijo parmesão": "100g", "leite integral": "1 caixa", "óleo vegetal": "1 garrafa", "queijo minas padrão": "1 pacote", "polvilho doce": "1 pacote", "manteiga sem sal": "1 tablete", "sal": "1 pacote", "pimenta do reino": "1 pote"}}
'''
new_recipe = splitResponse(response)

print(new_recipe.Grocery)
print(new_recipe.Recipe)