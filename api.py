from fastapi import FastAPI
from fastapi.responses import FileResponse
import json
import random
import subprocess

app = FastAPI()

# carregar banco de perguntas
with open("banco_perguntas.json", "r", encoding="utf-8") as f:
    perguntas = json.load(f)

# carregar usuarios
try:
    with open("usuarios.json", "r", encoding="utf-8") as f:
        usuarios = json.load(f)
except:
    usuarios = []

# ---------------------------
# REGISTRAR USUARIO
# ---------------------------
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

# ---------------------------
# LOGIN
# ---------------------------
@app.post("/login")
def login(usuario: str, senha: str):

    for u in usuarios:
        if u["usuario"] == usuario and u["senha"] == senha:
            return {"mensagem": "Login realizado"}

    return {"erro": "Usuário ou senha incorretos"}

# ---------------------------
# GERAR PROVA
# ---------------------------
@app.get("/gerar_prova")
def gerar_prova(materia: str, quantidade: int):

    filtradas = []

    for p in perguntas:
        if p["materia"].lower() == materia.lower():
            filtradas.append(p)

    quantidade = min(quantidade, len(filtradas))

    prova = random.sample(filtradas, quantidade)

    return {
        "materia": materia,
        "questoes": prova
    }

# ---------------------------
# BAIXAR PDF
# ---------------------------
@app.get("/baixar_pdf")
def baixar_pdf(materia: str, quantidade: int):

    subprocess.run(["python", "gerar_pdf.py", materia, str(quantidade)])

    return FileResponse(
        "prova.pdf",
        media_type="application/pdf",
        filename="prova.pdf"
    )

# ---------------------------
# CORRIGIR PROVA
# ---------------------------
@app.post("/corrigir_prova")
def corrigir_prova(respostas: list):

    acertos = 0

    for r in respostas:

        for p in perguntas:

            if p["pergunta"] == r["pergunta"]:

                if p["resposta"] == r["resposta"]:
                    acertos += 1

    total = len(respostas)

    nota = (acertos / total) * 10 if total > 0 else 0

    return {
        "acertos": acertos,
        "total": total,
        "nota": round(nota, 2)
    }