import json
import random

with open("banco_perguntas.json", "r", encoding="utf-8") as f:
    perguntas = json.load(f)

materia = input("Escolha a matéria: ")

quantidade = int(input("Quantas perguntas na prova? "))

filtradas = []

for p in perguntas:
    if p["materia"] == materia:
        filtradas.append(p)

# evita erro se pedir mais perguntas do que existem
quantidade = min(quantidade, len(filtradas))

prova = random.sample(filtradas, quantidade)

print("\nPROVA DO ALUNO\n")

for i, p in enumerate(prova,1):

    print(f"{i}. {p['pergunta']}")

    for j, opcao in enumerate(p["opcoes"],1):
        print(f"   {j}. {opcao}")

    print()

print("\nGABARITO\n")

for i, p in enumerate(prova,1):
    print(f"{i}. {p['resposta']}")