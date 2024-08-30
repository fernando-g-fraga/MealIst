import requests
import json
import os
import util

token = os.getenv("TODOIST_API_KEY_DEV")
header = {'Authorization':f"Bearer {token}"}
# teste = requests.get(f"https://api.todoist.com/rest/v2/projects",headers=header)

# print (teste.content)

def SearchGroceryList ():
    all_projects = requests.get(f"https://api.todoist.com/rest/v2/projects",headers=header).json()
    existent = False
    
    for obj in all_projects:
        new_dict = dict(obj)
        if new_dict.get('name')== "Grocery List":
            existent = True
            return new_dict.get('id')
        continue
    return existent
    
def createGroceryList(existent : bool) -> int:
    data ={ 
    "name":"Grocery List",
    "view_style":"List",
}
    if not existent:
        grocery_list = dict(requests.post(f"https://api.todoist.com/rest/v2/projects",headers=header,data=data).json)

        if grocery_list.status_code != 200:
            print(f"Error! {grocery_list.status_code}")
    return grocery_list.get("id")

def createGroceryList(grocery : dict)->str:
    grocery_id = SearchGroceryList()
    for key,value in grocery.items():
        data = {
        "content":f"{key} : {value}",
        "project_id": grocery_id
    }
        res = requests.post(f"https://api.todoist.com/rest/v2/tasks",data=data,headers=header)

    return res.status_code
        

grocerylist = createGroceryList(util.grocery)
print(grocerylist)
    