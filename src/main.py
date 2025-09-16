
import time
import random
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def calcular_elevado_quadrado_aleatorio():
    numero = random.randint(1,20)
    return {"quadrado_numero": numero ** 2}

@app.post("/calculate")
def calcular_elevado_quadrado(numero: int):
    return {"quadrado_numero": numero ** 2}


