import requests
import json
import os
import handler.util

token = os.getenv("TODOIST_API_KEY_DEV")
header = {'Authorization':f"Bearer {token}"}
# teste = requests.get(f"https://api.todoist.com/rest/v2/projects",headers=header)

# print (teste.content)

def SearchGroceryList ():
    """Search for the project Grocery List that will receive the shopping list for the generated recipes.
    It takes nothing and returns either an int ID or a Bool FALSE. """
    all_projects = dict(requests.get(f"https://api.todoist.com/rest/v2/projects",headers=header)).json()

    for obj in all_projects: #it could be faster if i search in a string? rather than convert to a dict? Maybe...we look into this later.
        new_dict = dict(obj)
        if new_dict.get('name')== "Grocery List":
            return new_dict.get('id')
        continue
     
    try: #The error handling are sh**, i'll work on that on project later stages.
        id_groceryList = postGroceryListProject()
    except:
        id_groceryList
    
def postGroceryListProject() -> int:
    """Creates a new project called Grocery List that will receive the shopping items for the generated recipes.
    It takes a bool as paramether, and returns an an INT ID or STRING error"""
    data ={ 
    "name":"Grocery List",
    "view_style":"List",
}   
    res = requests.post(f"https://api.todoist.com/rest/v2/projects",headers=header,data=data)
    grocery_list = dict(res.json)

    if res.status_code != 200:
        return res.raise_for_status()
    return grocery_list.get("id")

def postGroceryListTask(grocery : dict)->str:
   
    if SearchGroceryList() == type(int): grocery_id = SearchGroceryList()
    for key,value in grocery.items():
        data = {
        "content":f"{key} : {value}",
        "project_id": grocery_id
    } 
        res = requests.post(f"https://api.todoist.com/rest/v2/tasks",data=data,headers=header)

    return f"Ocorreu um erro ao criar o projeto Grocery List: {res.status_code}"


def SearchWeeklyMeal ():
    """Search for the project called WeeklyMeal with the meal prep and returns the INT ID, if not found will return false"""
    all_projects = requests.get(f"https://api.todoist.com/rest/v2/projects",headers=header).json()
    existent = False
    
    for project in all_projects:
        new_dict = dict(project)
        if new_dict.get('name')== "Weekly List":
            existent = True
            return new_dict.get('id')
        continue
    return existent

def postWeeklyMealProject(existent : bool) -> int:
    """Create a WeeklyMeal Project and return the INT ID, if not succced will return a STRING error"""
    data ={ 
    "name":"Weekly Meal",
    "view_style":"List",
}
    if not existent:
        req = requests.post(f"https://api.todoist.com/rest/v2/projects",headers=header,data=data)
        grocery_list = dict(req.json)
        existent = False
        if req.status_code != 200:
            print(f"Error! {grocery_list.status_code}")
            return f"Ocorreu um erro ao criar o projeto WeeklyMeal: {grocery_list.status}"
    return grocery_list.get("id")






# def postWeeklyMealTasks(meal : dict)->str:
    
#     if SearchWeeklyMeal() == type(int):
#         id_weeklymeal = grocerylist()
    

#     i = 0
#     while i < len(meal):
#         data = {
#         "content":f"{meal.get("name")}",
#         "description": f"{meal.get("ingredients")} \n {meal.get("instructions")}",
#         "project_id": weeklymeal_id
#     } 
#         res = requests.post(f"https://api.todoist.com/rest/v2/tasks",data=data,headers=header)
#         if res.status_code == 200: 
#             print(f"{meal.get("name")} salvo com sucesso!")
#         else: 
#             print(f"Falha em salvar a receita {meal.get("name")}")
#         i=+ 1
#     return res.status_code
        

# grocerylist = createGroceryList(util.grocery)
# print(grocerylist)
    