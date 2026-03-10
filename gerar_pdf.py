import json
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

with open("banco_perguntas.json", "r", encoding="utf-8") as f:
    perguntas = json.load(f)

materia = input("Escolha a matéria: ")
quantidade = int(input("Quantas perguntas na prova? "))

filtradas = []

for p in perguntas:
    if p["materia"] == materia:
        filtradas.append(p)

quantidade = min(quantidade, len(filtradas))

prova = random.sample(filtradas, quantidade)

# criar PDF
pdf = canvas.Canvas("prova.pdf", pagesize=letter)

y = 750

pdf.setFont("Helvetica", 12)
pdf.drawString(100, y, f"Prova de {materia}")

y -= 40

for i, p in enumerate(prova,1):

    pdf.drawString(100, y, f"{i}. {p['pergunta']}")
    y -= 20

    for opcao in p["opcoes"]:
        pdf.drawString(120, y, f"- {opcao}")
        y -= 20

    y -= 10

pdf.save()

print("PDF da prova criado com sucesso!")