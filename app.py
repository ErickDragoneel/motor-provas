import random
import json

# GERAR PERGUNTA DE MATEMÁTICA
def gerar_matematica():

    a = random.randint(2,20)
    b = random.randint(2,20)

    resposta = a * b

    opcoes = [
        resposta,
        resposta + random.randint(1,10),
        resposta - random.randint(1,10),
        resposta + random.randint(5,15)
    ]

    random.shuffle(opcoes)

    return {
        "materia": "Matemática",
        "pergunta": f"Quanto é {a} x {b}?",
        "opcoes": opcoes,
        "resposta": resposta
    }


# BANCO DE PERGUNTAS DE GEOGRAFIA
geografia = [
    {
        "pergunta": "Qual é a capital do Brasil?",
        "opcoes": ["São Paulo","Brasília","Rio de Janeiro","Salvador"],
        "resposta": "Brasília"
    },
    {
        "pergunta": "Qual é o maior oceano do mundo?",
        "opcoes": ["Atlântico","Índico","Pacífico","Ártico"],
        "resposta": "Pacífico"
    }
]


# BANCO DE PERGUNTAS DE HISTÓRIA
historia = [
    {
        "pergunta": "Quem descobriu o Brasil?",
        "opcoes": ["Pedro Álvares Cabral","Dom Pedro","Cristóvão Colombo","Tiradentes"],
        "resposta": "Pedro Álvares Cabral"
    },
    {
        "pergunta": "Em que ano o Brasil foi descoberto?",
        "opcoes": ["1492","1500","1822","1889"],
        "resposta": "1500"
    }
]


def gerar_banco(quantidade):

    banco = []

    for _ in range(quantidade):

        materia = random.choice(["Matemática","Geografia","História"])

        if materia == "Matemática":
            banco.append(gerar_matematica())

        elif materia == "Geografia":
            p = random.choice(geografia)
            banco.append({
                "materia":"Geografia",
                "pergunta":p["pergunta"],
                "opcoes":p["opcoes"],
                "resposta":p["resposta"]
            })

        elif materia == "História":
            p = random.choice(historia)
            banco.append({
                "materia":"História",
                "pergunta":p["pergunta"],
                "opcoes":p["opcoes"],
                "resposta":p["resposta"]
            })


    with open("banco_perguntas.json","w",encoding="utf-8") as f:
        json.dump(banco,f,indent=4,ensure_ascii=False)

    print("Banco de perguntas criado!")


gerar_banco(500)