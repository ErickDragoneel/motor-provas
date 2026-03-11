import json
import random

def gerar_matematica_fundamental():

    perguntas = []

    for i in range(200):

        a = random.randint(1,20)
        b = random.randint(1,20)

        resposta = a * b

        opcoes = [
            resposta,
            resposta + random.randint(1,5),
            resposta - random.randint(1,5),
            resposta + random.randint(6,10)
        ]

        random.shuffle(opcoes)

        pergunta = {
            "materia": "Matemática",
            "nivel": "Fundamental 7",
            "dificuldade": "facil",
            "pergunta": f"Quanto é {a} × {b} ?",
            "opcoes": opcoes,
            "resposta": resposta
        }

        perguntas.append(pergunta)

    return perguntas


with open("banco_perguntas.json","r",encoding="utf-8") as f:
    banco = json.load(f)

novas = gerar_matematica_fundamental()

banco.extend(novas)

with open("banco_perguntas.json","w",encoding="utf-8") as f:
    json.dump(banco,f,indent=4,ensure_ascii=False)

print("Perguntas adicionadas com sucesso")