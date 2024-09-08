import requests
import json
import os
from handler.util import get_WeekArray
import datetime as d

token = os.getenv("TODOIST_API_KEY_DEV")
header = {'Authorization':f"Bearer {token}"}

def SearchGroceryList ():
    """Search for the project Grocery List that will receive the shopping list for the generated recipes.
    It takes nothing and returns either an int ID or a Bool FALSE. """
    all_projects = requests.get(f"https://api.todoist.com/rest/v2/projects",headers=header).json()

    for obj in all_projects: #it could be faster if i search in a string? rather than convert to a dict? Maybe...we look into this later.  
        if obj.get('name')== "Grocery List":
            return obj.get('id')
        continue
    return None

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
    grocery_id = SearchGroceryList()

    if grocery_id != None: 
        for key,value in grocery.items():
            data = {
            "content":f"{key} : {value}",
            "project_id": grocery_id
        } 
            res = requests.post(f"https://api.todoist.com/rest/v2/tasks",data=data,headers=header)
        

def SearchWeeklyMealProject ():
    """Search for the project called WeeklyMeal with the meal prep and returns the INT ID, if not found will return false"""
    all_projects = requests.get(f"https://api.todoist.com/rest/v2/projects",headers=header).json()
   
    for project in all_projects:
        if project.get('name') == "Weekly List":
            return project.get("id")
        continue
    return None 

def postWeeklyMealProject():
    """Create a WeeklyMeal Project and return the INT ID, if not succced will return a STRING error"""
    data ={ 
    "name":"Weekly Meal",
    "view_style":"List",
}
    req = dict(requests.post(f"https://api.todoist.com/rest/v2/projects",headers=header,data=data).json)
    grocery_list = dict(req.json)

    if req.status_code != 200:
        print(f"Error! {grocery_list.status_code}")
        return f"Ocorreu um erro ao criar o projeto WeeklyMeal: {grocery_list.status}"
    return grocery_list.get("id")


def postWeeklyMealTasks(weekly_meal : dict)->str:

    id_weeklymeal = SearchWeeklyMealProject()
    
    if id_weeklymeal != None:
        weekArray = get_WeekArray(weekly_meal)
    else:
        postWeeklyMealProject() #it should be abstracted on other function. Will do later. 

    for index,recipe in enumerate(weekly_meal):
        data = {
        "content":f"{weekly_meal[index].get("name")}",
        "description": f"{weekly_meal[index].get("ingredients")} \n {weekly_meal[index].get("instructions")}",
        "project_id": id_weeklymeal,
        "due":{
            "date":(f"{weekArray[index]} at 12:00 PM - Lunch {weekly_meal[index].get("name")}" )
            },
    } 
        res = requests.post(f"https://api.todoist.com/rest/v2/tasks",data=data,headers=header)

        if res.status_code == 200: 
            print(f"{weekly_meal[index].get("name")} salvo com sucesso!")
        else: 
            print(f"Falha em salvar a receita {weekly_meal.get("name")} | {res.status_code}")
    
    return id_weeklymeal
        