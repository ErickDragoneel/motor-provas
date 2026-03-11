from fastapi import FastAPI
from fastapi.responses import FileResponse
import json
import random
import subprocess

app = FastAPI()

with open("banco_perguntas.json", "r", encoding="utf-8") as f:
    perguntas = json.load(f)

try:
    with open("usuarios.json", "r", encoding="utf-8") as f:
        usuarios = json.load(f)
except:
    usuarios = []


@app.post("/registrar")
def registrar(usuario: str, senha: str):

    novo = {
        "usuario": usuario,
        "senha": senha
    }

    usuarios.append(novo)

    with open("usuarios.json", "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4)

    return {"mensagem": "Usuário criado com sucesso"}


@app.post("/login")
def login(usuario: str, senha: str):

    for u in usuarios:
        if u["usuario"] == usuario and u["senha"] == senha:
            return {"mensagem": "Login realizado"}

    return {"erro": "Usuário ou senha incorretos"}


@app.get("/gerar_prova")
def gerar_prova(materia: str, nivel: str, quantidade: int):

    filtradas = []

    for p in perguntas:
        if (
            p["materia"].lower() == materia.lower()
            and p["nivel"].lower() == nivel.lower()
        ):
            filtradas.append(p)

    quantidade = min(quantidade, len(filtradas))

    prova = random.sample(filtradas, quantidade)

    return {
        "materia": materia,
        "nivel": nivel,
        "questoes": prova
    }


@app.get("/baixar_pdf")
def baixar_pdf(materia: str, nivel: str, quantidade: int):

    subprocess.run(["python", "gerar_pdf.py", materia, nivel, str(quantidade)])

    return FileResponse(
        "prova.pdf",
        media_type="application/pdf",
        filename="prova.pdf"
    )