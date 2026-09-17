# Washington Oliveira — Portfólio

Site institucional de uma página para apresentar o trabalho de Washington Oliveira em design, código e imagem.

## Rodar localmente

```bash
cd washington_portfolio
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

Abra `http://127.0.0.1:5000`.

## Organização

- `run.py`: entrada para desenvolvimento e Gunicorn.
- `config.py`: configurações e caminho do SQLite.
- `app/routes.py`: rotas da aplicação.
- `app/templates/`: HTML com Jinja2.
- `app/static/css/`: identidade visual e responsividade.
- `app/static/js/`: animação de entrada ao rolar a página.
- `app/db.py`: conexão e inicialização do SQLite.

Para publicar no Railway, envie esta pasta como projeto. O `Dockerfile` já
define a imagem Python e evita o instalador `mise`; o comando usa a porta
fornecida pelo Railway. O `Procfile` continua disponível para hosts que usam
detecção tradicional de projetos Python.

No Railway, confirme que `Dockerfile` está na raiz do serviço e faça um novo
deploy. Se aparecer opção de cache, escolha limpar o cache do build.
