import sys
import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from openai import OpenAI

client = OpenAI(api_key="SUA_CHAVE_AQUI")

materia = sys.argv[1]
nivel = sys.argv[2]
tema = sys.argv[3]
dificuldade = sys.argv[4]
quantidade = int(sys.argv[5])

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
    print("Erro ao gerar")
    exit()

pdf = canvas.Canvas("prova.pdf", pagesize=letter)

y = 750

pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(100, y, f"Prova de {materia}")

y -= 30
pdf.setFont("Helvetica", 12)
pdf.drawString(100, y, f"Nível: {nivel}")

y -= 20
pdf.drawString(100, y, f"Tema: {tema}")

y -= 20
pdf.drawString(100, y, f"Dificuldade: {dificuldade}")

y -= 40
pdf.drawString(100, y, "Aluno: __________________________")

y -= 30
pdf.drawString(100, y, "Data: ____ / ____ / ______")

y -= 40

for i, q in enumerate(questoes, 1):

    pdf.drawString(100, y, f"{i}. {q['pergunta']}")
    y -= 20

    for op in q["opcoes"]:
        pdf.drawString(120, y, f"( ) {op}")
        y -= 20

    y -= 10

    if y < 100:
        pdf.showPage()
        y = 750

pdf.save()