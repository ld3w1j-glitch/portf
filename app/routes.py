from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.get("/")
def index():
    projects = [
        {"number": "01", "title": "Identidade visual", "kind": "Branding", "description": "Sistemas de marca que organizam presença, linguagem e reconhecimento."},
        {"number": "02", "title": "Produtos digitais", "kind": "Web & código", "description": "Interfaces úteis, claras e com personalidade para negócios reais."},
        {"number": "03", "title": "Imagem em movimento", "kind": "Motion design", "description": "Apresentações e narrativas visuais para explicar ideias com ritmo."},
    ]
    return render_template("index.html", projects=projects)
