import json
import random


def gerar_matematica():

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


def gerar_historia():

    base = [
        ("Quem descobriu o Brasil?", ["Pedro Álvares Cabral","Dom Pedro","Tiradentes","Getúlio Vargas"], "Pedro Álvares Cabral"),
        ("Em que ano o Brasil foi descoberto?", ["1500","1492","1822","1889"], "1500"),
        ("Quem foi o primeiro imperador do Brasil?", ["Dom Pedro I","Dom Pedro II","Cabral","Tiradentes"], "Dom Pedro I"),
    ]

    perguntas = []

    for i in range(100):

        p = random.choice(base)

        pergunta = {
            "materia": "História",
            "nivel": "Fundamental 7",
            "dificuldade": "facil",
            "pergunta": p[0],
            "opcoes": p[1],
            "resposta": p[2]
        }

        perguntas.append(pergunta)

    return perguntas


def gerar_geografia():

    base = [
        ("Qual é o maior país da América do Sul?", ["Brasil","Argentina","Chile","Peru"], "Brasil"),
        ("Qual é o maior oceano do mundo?", ["Pacífico","Atlântico","Índico","Ártico"], "Pacífico"),
        ("Qual é a capital da França?", ["Paris","Roma","Madri","Lisboa"], "Paris"),
    ]

    perguntas = []

    for i in range(100):

        p = random.choice(base)

        pergunta = {
            "materia": "Geografia",
            "nivel": "Fundamental 7",
            "dificuldade": "facil",
            "pergunta": p[0],
            "opcoes": p[1],
            "resposta": p[2]
        }

        perguntas.append(pergunta)

    return perguntas


def gerar_portugues():

    base = [
        ("Qual é o plural de pão?", ["pães","paes","pãos","pãeses"], "pães"),
        ("Qual é o feminino de ator?", ["atriz","atora","atorisa","atrosa"], "atriz"),
        ("Qual palavra é um verbo?", ["correr","azul","mesa","rápido"], "correr"),
    ]

    perguntas = []

    for i in range(100):

        p = random.choice(base)

        pergunta = {
            "materia": "Português",
            "nivel": "Fundamental 7",
            "dificuldade": "facil",
            "pergunta": p[0],
            "opcoes": p[1],
            "resposta": p[2]
        }

        perguntas.append(pergunta)

    return perguntas


# carregar banco atual

with open("banco_perguntas.json","r",encoding="utf-8") as f:
    banco = json.load(f)


novas = []
novas.extend(gerar_matematica())
novas.extend(gerar_historia())
novas.extend(gerar_geografia())
novas.extend(gerar_portugues())


banco.extend(novas)


with open("banco_perguntas.json","w",encoding="utf-8") as f:
    json.dump(banco,f,indent=4,ensure_ascii=False)


print("Perguntas geradas com sucesso")