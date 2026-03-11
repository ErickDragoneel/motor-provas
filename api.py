from fastapi import FastAPI
from fastapi.responses import FileResponse
import json
import random
import subprocess

app = FastAPI()

with open("banco_perguntas.json", "r", encoding="utf-8") as f:
    perguntas = json.load(f)


@app.get("/gerar_prova")
def gerar_prova(materia: str, nivel: str, dificuldade: str, quantidade: int):

    filtradas = []

    for p in perguntas:
        if (
            p["materia"].lower() == materia.lower()
            and p["nivel"].lower() == nivel.lower()
            and p["dificuldade"].lower() == dificuldade.lower()
        ):
            filtradas.append(p)

    quantidade = min(quantidade, len(filtradas))

    prova = random.sample(filtradas, quantidade)

    return {
        "materia": materia,
        "nivel": nivel,
        "dificuldade": dificuldade,
        "questoes": prova
    }


@app.get("/baixar_pdf")
def baixar_pdf(materia: str, nivel: str, dificuldade: str, quantidade: int):

    subprocess.run(["python", "gerar_pdf.py", materia, nivel, dificuldade, str(quantidade)])

    return FileResponse(
        "prova.pdf",
        media_type="application/pdf",
        filename="prova.pdf"
    )