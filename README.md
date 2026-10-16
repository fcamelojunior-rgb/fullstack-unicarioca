# Laboratório Full Stack UniCarioca

Projeto acadêmico de Ciência da Computação que integra frontend HTML, API REST com FastAPI, banco de dados SQLite e Docker Compose.

Laboratório Full Stack da UniCarioca — Ciência da Computação.

## Arquitetura

- **Frontend:** HTML, CSS e JavaScript servidos pelo Nginx.
- **Backend:** Python, FastAPI e Uvicorn.
- **Comunicação:** o navegador faz requisições HTTP para a API.
- **Banco de dados:** SQLite armazena os projetos.
- **Contêineres:** Docker e Docker Compose sobem frontend e backend juntos.
- **Persistência:** o volume Docker `sqlite_data` guarda o arquivo do banco entre reinicializações dos contêineres.

O aluno abre a página, clica em **Carregar projetos** e o JavaScript consulta `http://localhost:8000/projects`. A API lê o SQLite e devolve a lista.

## Endereços locais

- Frontend: [http://localhost:8080](http://localhost:8080)
- API: [http://localhost:8000](http://localhost:8000)
- Projetos: [http://localhost:8000/projects](http://localhost:8000/projects)
- Documentação interativa da API: [http://localhost:8000/docs](http://localhost:8000/docs)

Use `http://localhost:8080` (não `127.0.0.1`) para a página coincidir com a origem liberada pela API.

## Como executar

Na raiz do projeto:

```
docker compose up --build
```

Abra [http://localhost:8080](http://localhost:8080) e clique em **Carregar projetos**.

Para interromper os serviços, pressione `Ctrl+C` no terminal em que o Docker Compose está sendo executado.

Para executar os contêineres em segundo plano:

```
docker compose up -d
```

Para pará-los sem remover o volume de dados:

```
docker compose stop
```

O comando `docker compose down -v` remove o volume `sqlite_data` e apaga os dados do banco.

## Estrutura do projeto

- `frontend/`: `index.html`, `style.css` e `app.js`. No Compose, o Nginx usa esta pasta.
- `backend/app/`: API FastAPI (`main.py`) e acesso ao SQLite (`database.py`).
- `backend/Dockerfile` e `backend/requirements.txt`: imagem e dependências da API.
- `docker-compose.yml`: serviços, portas e volume persistente.
- `.gitignore`: arquivos locais ignorados pelo Git.
- `AGENTS.md`: orientações para o agente de IA que auxilia no laboratório.

## Status

- Frontend funcional.
- API REST com FastAPI.
- Integração frontend-backend.
- Contêineres configurados com Docker Compose.
- Repositório Git e publicação no GitHub.
- Persistência de dados com SQLite.
- Revisão técnica com o agente de IA do Cursor.
