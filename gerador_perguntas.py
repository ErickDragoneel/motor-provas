import random
import json

# ---------- MATEMÁTICA ----------

def gerar_matematica():

    a = random.randint(1, 50)
    b = random.randint(1, 50)

    pergunta = f"Quanto é {a} + {b}?"
    resposta = a + b

    opcoes = [
        resposta,
        resposta + random.randint(1,5),
        resposta - random.randint(1,5),
        resposta + random.randint(2,10)
    ]

    random.shuffle(opcoes)

    return {
        "materia": "Matemática",
        "pergunta": pergunta,
        "opcoes": opcoes,
        "resposta": resposta
    }

# ---------- HISTÓRIA ----------

def gerar_historia():

    perguntas = [
        ("Em que ano o Brasil foi descoberto?", ["1500","1492","1822","1889"], "1500"),
        ("Quem foi o primeiro presidente do Brasil?", ["Deodoro da Fonseca","Getúlio Vargas","Dom Pedro II","Juscelino Kubitschek"], "Deodoro da Fonseca"),
        ("Qual evento ocorreu em 1822?", ["Independência do Brasil","Proclamação da República","Descobrimento do Brasil","Fim da escravidão"], "Independência do Brasil")
    ]

    p = random.choice(perguntas)

    return {
        "materia": "História",
        "pergunta": p[0],
        "opcoes": p[1],
        "resposta": p[2]
    }

# ---------- GEOGRAFIA ----------

def gerar_geografia():

    perguntas = [
        ("Qual é o maior país da América do Sul?", ["Brasil","Argentina","Chile","Peru"], "Brasil"),
        ("Qual é o maior oceano do mundo?", ["Pacífico","Atlântico","Índico","Ártico"], "Pacífico"),
        ("Qual é a capital da França?", ["Paris","Roma","Madrid","Lisboa"], "Paris")
    ]

    p = random.choice(perguntas)

    return {
        "materia": "Geografia",
        "pergunta": p[0],
        "opcoes": p[1],
        "resposta": p[2]
    }

# ---------- GERADOR GERAL ----------

def gerar_pergunta():

    geradores = [
        gerar_matematica,
        gerar_historia,
        gerar_geografia
    ]

    gerador = random.choice(geradores)

    return gerador()


def gerar_varias(qtd):

    lista = []

    for _ in range(qtd):
        lista.append(gerar_pergunta())

    return lista


if __name__ == "__main__":

    novas = gerar_varias(30)

    with open("banco_perguntas.json", "r", encoding="utf-8") as f:
        banco = json.load(f)

    banco.extend(novas)

    with open("banco_perguntas.json", "w", encoding="utf-8") as f:
        json.dump(banco, f, indent=4, ensure_ascii=False)

    print("Novas perguntas adicionadas!")