from fastapi import FastAPI
from fastapi.responses import FileResponse
import subprocess
import json
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key="SUA_CHAsk-proj-gpLZBNtSTCR9bGhBFtBJs_6_aC9q0VBzTdGtwRfevsWvfp21yBfQO_-gwJIFw1kUmJQHpuPyyAT3BlbkFJPecl-s-MJMi5qrM6WwlW--5YPLjYr4i1hcomz4lFeVN7l-5rWo2GiwHmj8tRONml02yTdZ8ccAVE_AQUI")

# ===== GERAR PROVA COM IA =====

@app.get("/gerar_prova")
def gerar_prova(materia: str, nivel: str, tema: str, dificuldade: str, quantidade: int):

    prompt = f"""
    Gere {quantidade} questões de {materia} para {nivel},
    tema {tema}, dificuldade {dificuldade}.

    Formato JSON:
    [
      {{
        "pergunta": "...",
        "opcoes": ["A","B","C","D"],
        "resposta": "..."
      }}
    ]
    """

    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    texto = resposta.choices[0].message.content

    try:
        questoes = json.loads(texto)
    except:
        return {"erro": "Erro ao gerar perguntas"}

    return {
        "materia": materia,
        "nivel": nivel,
        "tema": tema,
        "dificuldade": dificuldade,
        "questoes": questoes
    }


# ===== BAIXAR PDF =====

@app.get("/baixar_pdf")
def baixar_pdf(materia: str, nivel: str, tema: str, dificuldade: str, quantidade: int):

    # chama o script com IA
    subprocess.run(["python", "gerar_pdf.py", materia, nivel, tema, dificuldade, str(quantidade)])

    return FileResponse(
        "prova.pdf",
        media_type="application/pdf",
        filename="prova.pdf"
    )