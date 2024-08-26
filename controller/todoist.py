import requests
import json
import os

token = os.getenv("TODOIST_API_KEY_DEV")
header = {'Authorization':f"Bearer {token}"}
# teste = requests.get(f"https://api.todoist.com/rest/v2/projects",headers=header)

# print (teste.content)

def getOrCreateProjects ():
    data ={ 
    "name":"Grocery List",
    "view_style":"List",
}
    all_projects = requests.get(f"https://api.todoist.com/rest/v2/projects",headers=header).json()
    existent = False
    
    for obj in all_projects:
        new_dict = dict(obj)
        if new_dict.get('name')== "Grocery List":
            existent = True
            break
        continue
    
    if not existent:
        try:
            create_project = requests.post(f"https://api.todoist.com/rest/v2/projects",headers=header,data=data)
        except:
            print(f"Error! {create_project.status_code}")
        

teste = getOrCreateProjects()
print(teste)