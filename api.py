from fastapi.responses import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile


@app.get("/prova_pdf")
def gerar_pdf(materia: str, quantidade: int):

    filtradas = []

    for p in perguntas:
        if p["materia"].lower() == materia.lower():
            filtradas.append(p)

    quantidade = min(quantidade, len(filtradas))

    prova = random.sample(filtradas, quantidade)

    arquivo = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    pdf = canvas.Canvas(arquivo.name, pagesize=letter)

    y = 750

    pdf.drawString(100, y, f"Prova de {materia}")

    y -= 40

    for i, p in enumerate(prova, 1):

        pdf.drawString(100, y, f"{i}. {p['pergunta']}")
        y -= 20

        for op in p["opcoes"]:
            pdf.drawString(120, y, f"- {op}")
            y -= 20

        y -= 10

    pdf.save()

    return FileResponse(arquivo.name, filename="prova.pdf")