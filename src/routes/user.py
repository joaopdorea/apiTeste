import time
import random
from fastapi import FastAPI, HTTPException
from src.model.user import User

from src.controller.user import c_get_user, c_create_user, c_delete_user, c_update_user


app = FastAPI()


#retornando o usuário a partir do userId
@app.get("/users/{user_id}")
async def getUser(user_id: int):
    resposta = await c_get_user(user_id)
    if not resposta:
        raise HTTPException(status_code = 404, detail = "Usuário Não Encontrado")
    return resposta
     

@app.post("/users")
async def createUser(user: User):
    resposta = await c_get_user(user.id)
    if resposta:
        raise HTTPException(status_code = 404, detail = "Usuário já cadastrado")
    await c_create_user(user)
    return 

@app.delete("/users/{user_id}")
async def deleteUser(user_id: int):
    resposta = await c_get_user(user_id)
    if not resposta:
        raise HTTPException(status_code = 404, detail = "Usuário Não Encontrado")
    await c_delete_user(user_id)
    return

@app.put("/users/{user_id}")
async def updateUser(user_id: int, user: User):
    resposta = await c_get_user(user.id)
    if not resposta:
        raise HTTPException(status_code = 404, detail = "Usuário Não Encontrado")
    await c_update_user(user, user_id)
    return 




