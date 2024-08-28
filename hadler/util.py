import google.generativeai
import google.generativeai as genia

prompt_instructions = '''You will receive at least 1 recipe. Your goal is to create two json files: 
Recipes: {
name: mac n cheese, 
ingredients: ["ingredient1", "ingredient2", ...], 
directions: ["step 1 - ..."]} 
Grocery_shop: {"milk": 2 boxes, "eggs": 6 eggs}. 
All the responses should be in portuguese'''

model = genia.GenerativeModel("models/gemini-1.5-flash",system_instruction=prompt_instructions)

prompt = '''Receitas: Macarrão com queijo, Carne moída com batatas, Macarrão bolonhesa, Lasanha'''
res = model.generate_content(prompt)

print(res.text)
print(res.usage_metadata)