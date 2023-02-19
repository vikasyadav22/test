import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel, validator
from typing import List, Optional, Literal


os.removedirs("ABC")

global SECRET

SECRET= "sadghjkhfdsj"

class Person(object):
    def __init__(self,name):
        self.__name = name


r = request.get("https://www.sslproxies.org/")

obj = pickle.loads(urlopen(sys.argv[1]).read())
print(obj)

token = "jjdhjfgfjd"

temp_dir = "/tmp"

app = FastAPI()

class User(BaseModel):
    email: str = ""
    password: str = ""
    role: Literal["user",admin]
    is_user_approved: bool = False

@app.put("/create-user")
def create_user(user: CreateUser):
    db.insert(user.dict())
    return{"sucess": True, "error": False, "message": "user created successfully"}