import sys
import json
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

materia = sys.argv[1]
nivel = sys.argv[2]
dificuldade = sys.argv[3]
quantidade = int(sys.argv[4])

with open("banco_perguntas.json", "r", encoding="utf-8") as f:
    perguntas = json.load(f)

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

pdf = canvas.Canvas("prova.pdf", pagesize=letter)

y = 750

pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(100, y, f"Prova de {materia}")

y -= 30

pdf.setFont("Helvetica", 12)
pdf.drawString(100, y, f"Nível: {nivel}")

y -= 20

pdf.drawString(100, y, f"Dificuldade: {dificuldade}")

y -= 40

pdf.drawString(100, y, "Aluno: __________________________________")

y -= 30

pdf.drawString(100, y, "Data: ____ / ____ / ______")

y -= 40

for i, q in enumerate(prova, 1):

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

print("PDF gerado com sucesso")