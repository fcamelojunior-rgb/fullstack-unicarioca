# Laboratório Full Stack UniCarioca

Projeto acadêmico de Ciência da Computação que integra frontend HTML, API REST com FastAPI, banco de dados SQLite e Docker Compose.

## Arquitetura

- **Frontend:** HTML, CSS e JavaScript servido pelo Nginx.
- **Backend:** Python, FastAPI e Uvicorn.
- **Comunicação:** requisições HTTP entre frontend e API.
- **Banco de dados:** SQLite para armazenamento persistente dos projetos.
- **Contêineres:** Docker e Docker Compose.
- **Persistência:** volume Docker nomeado para preservar o banco de dados entre reinicializações dos contêineres.

## Endereços locais

- Frontend: [http://localhost:8080](http://localhost:8080)
- API: [http://localhost:8000](http://localhost:8000)
- Projetos: [http://localhost:8000/projects](http://localhost:8000/projects)
- Documentação interativa da API: [http://localhost:8000/docs](http://localhost:8000/docs)

## Como executar

Na raiz do projeto, execute:

```
docker compose up --build
```

Abra [http://localhost:8080](http://localhost:8080) e clique em **Carregar projetos**.

Para interromper os serviços, pressione `Ctrl+C` no terminal em que o Docker Compose está sendo executado.

Para executar os contêineres em segundo plano, utilize:

```
docker compose up -d
```

Para pará-los sem remover o volume de dados:

```
docker compose stop
```

## Estrutura do projeto

- `backend/`: API FastAPI, dependências e Dockerfile.
- `frontend/`: página HTML e Dockerfile.
- `docker-compose.yml`: configuração dos serviços e do volume persistente.
- `.gitignore`: arquivos locais ignorados pelo Git.

## Status

- Frontend funcional.
- API REST com FastAPI.
- Integração frontend-backend.
- Contêineres configurados com Docker Compose.
- Repositório Git e publicação no GitHub.
- Persistência de dados com SQLite.
- Revisão técnica com o agente de IA do Cursor.

## Contexto acadêmico

Laboratório Full Stack da UniCarioca — Ciência da Computação.