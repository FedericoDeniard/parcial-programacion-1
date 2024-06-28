import json

def save_config(path: str,data: dict):
    with open(path,'w') as config:
        json.dump(data,config,indent=2)

def save_id(old_data: dict, id:int):
    old_data["last_id"] = id

def new_id(data: dict):
    last_id = data["last_id"]
    data["last_id"] = last_id + 1
    return data["last_id"]

def load_config(path: str) -> dict:
    with open(path,'r') as file:
        config = json.load(file)
    return config