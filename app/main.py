from fastapi import FastAPI
from datetime import datetime

myapp=FastAPI(title="my first AWS APP")

@myapp.get("/welcome")
def welcome_user():
    current_time=datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    return f'hey buddy welcome to our application, The time is {current_time}'

@myapp.post("/data")
def get_user_data(name:str):
    return f'hey {name} your resquest has been received successfully...'