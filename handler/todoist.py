import requests
import json
import os
from handler.util import get_WeekArray
import datetime as d

MEAL_PROJECT_NAME = "Meal Prep"
GROCERY_PROJECT_NAME = "Grocery List"

token = os.getenv("TODOIST_API_KEY_DEV")
header = {'Authorization':f"Bearer {token}"}

def SearchGroceryList ():
    """Search for the project Grocery List that will receive the shopping list for the generated recipes.
    It takes nothing and returns either an int ID or a Bool FALSE. """
    req = requests.get(f"https://api.todoist.com/rest/v2/projects",headers=header)
    parsedRes  = req.json()

    for obj in parsedRes:
        if obj.get('name')== GROCERY_PROJECT_NAME:
            return obj.get('id')
        continue
    return None

def postGroceryListProject() -> int:
    """Creates a new project called Grocery List that will receive the shopping items for the generated recipes.
    It takes a bool as paramether, and returns an an INT ID or STRING error"""
    data ={ 
    "name":GROCERY_PROJECT_NAME,
    "view_style":"List",
}   
    req = requests.post(f"https://api.todoist.com/rest/v2/projects",headers=header,data=data)
    res = req.json()

    if res.status_code != 200:
        return res.raise_for_status()
    return res.get("id")

def postGroceryListTask(grocery : dict)->str:
    grocery_id = SearchGroceryList()

    if grocery_id == None:
        grocery_id = postGroceryListProject() 
    
    for key,value in grocery.items():
        data = {
        "content":f"{key} : {value}",
        "project_id": grocery_id
    } 
        req = requests.post(f"https://api.todoist.com/rest/v2/tasks",data=data,headers=header)
        if  req.status_code == 200:
            print("Grocery Item Created!")
        else:
            print(f"Error on create the item. {req.status_code}")
            
    
    

def SearchWeeklyMealProject ():
    """Search for the project called WeeklyMeal with the meal prep and returns the INT ID, if not found will return false"""
    all_projects = requests.get(f"https://api.todoist.com/rest/v2/projects",headers=header).json()
   
    for project in all_projects:
        if project.get('name') == MEAL_PROJECT_NAME:
            return project.get("id")
        continue
    return None 

def postWeeklyMealProject():
    """Create a WeeklyMeal Project and return the INT ID, if not succced will return a STRING error"""
    data ={ 
    "name":MEAL_PROJECT_NAME,
    "view_style":"List",
}
    req = requests.post(f"https://api.todoist.com/rest/v2/projects",headers=header,data=data)
    parsedRes = req.json()

    if req.status_code != 200:
        return f"Ocorreu um erro ao criar o projeto WeeklyMeal: {req.status_code}"
    return parsedRes.get("id")


def postWeeklyMealTasks(weekly_meal : list[dict])->str:

    id_weeklymeal = SearchWeeklyMealProject()
    weekArray = get_WeekArray(weekly_meal)
    
    if id_weeklymeal == None:
       id_weeklymeal = postWeeklyMealProject()

    for i,meal in enumerate(weekly_meal):
        data = {
        "content":f"{meal.get("name")}",
        "description": f"{meal.get("ingredients")} \n {meal.get("instructions")}",
        "project_id": id_weeklymeal,
        "due":{
            "date":(f"{weekArray[i]} at 12:00 PM - Lunch {meal.get("name")}" )
            },
    } 
        res = requests.post(f"https://api.todoist.com/rest/v2/tasks",data=data,headers=header)

        if res.status_code == 200: 
            print(f"{meal.get("name")} salvo com sucesso!")
        else: 
            print(f"Falha em salvar a receita {meal.get("name")} | {res.status_code}")
    
    return id_weeklymeal
  