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