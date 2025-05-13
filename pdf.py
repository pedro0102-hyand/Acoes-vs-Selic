from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from datetime import datetime
import os

def gerar_pdf():
    os.makedirs('relatorio', exist_ok=True)
    nome_pdf = "relatorio/analise_final.pdf"
    c = canvas.Canvas(nome_pdf, pagesize=A4)
    width, height = A4

    # Cabeçalho
    c.setFont("Helvetica-Bold", 16)
    c.drawString(2*cm, height - 2*cm, "📊 Análise de Ações vs Selic (2010–2023)")

    c.setFont("Helvetica", 10)
    c.drawString(2*cm, height - 2.6*cm, f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    # Gráficos
    imagens = [
        "figuras/acoes_vs_selic.png",
        "figuras/correlacao_retorno.png",
        "figuras/cluster_risco_retorno.png",
        "figuras/correlacao_dinamica_ITUB4.png",
        "figuras/correlacao_dinamica_EMBR3.png",
        "figuras/correlacao_dinamica_VALE3.png",
    ]

    y = height - 4*cm
    for img in imagens:
        if os.path.exists(img):
            c.drawImage(img, 2*cm, y - 10*cm, width=17*cm, height=10*cm)
            y -= 11*cm
            if y < 5*cm:
                c.showPage()
                y = height - 3*cm

    # Rodapé
    c.setFont("Helvetica-Oblique", 8)
    c.drawString(2*cm, 1.5*cm, "Relatório gerado automaticamente com Python — Pedro Júlio © 2025")
    c.save()
    print(f"📄 PDF salvo com sucesso em: {nome_pdf}")

# Rodar direto
if __name__ == "__main__":
    gerar_pdf()