from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
import json


app = FastAPI()

origins = ["http://127.0.0.1:5500/", '*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/api")
def signIn(username: str, password: str):
    with open('passwords_db.json') as f:
        data = json.load(f)
    if username in data:
        raise HTTPException(status_code = 409, detail = 'Username is taken')
    else:
        if password in data.values():
            raise HTTPException(status_code = 409, detail = 'Password is taken')
        else:
            data[username] = password
            with open('passwords_db.json', 'w', encoding = 'utf-8') as f:
                json.dump(data, f, ensure_ascii = False, indent = 4)
            raise HTTPException(status_code = 200)


# @app.get("/api")
# def logIn(username: str, password: str):
#     with open('passwords_db.json') as f:
#         data = json.load(f)
#     if username in data:
#         return 