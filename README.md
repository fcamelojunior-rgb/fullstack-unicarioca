# Laboratório Full Stack UniCarioca

Projeto acadêmico de Ciência da Computação que integra frontend HTML, API REST com FastAPI e Docker Compose.

## Arquitetura

- Frontend: HTML, CSS e JavaScript servido pelo Nginx.
- Backend: Python, FastAPI e Uvicorn.
- Comunicação: HTTP entre frontend e API.
- Contêineres: Docker e Docker Compose.
- Banco de dados: SQLite, ainda pendente de implementação.

## Endereços locais

- Frontend: http://localhost:8080
- API: http://localhost:8000
- Projetos: http://localhost:8000/projects
- Documentação: http://localhost:8000/docs

## Como executar

Na raiz do projeto, execute:

    docker compose up --build

Abra http://localhost:8080 e clique em "Carregar projetos".

Para interromper os serviços, pressione Ctrl+C no terminal em que o Docker Compose está rodando.

## Estrutura do projeto

- backend/: API FastAPI e Dockerfile.
- frontend/: página HTML e Dockerfile.
- docker-compose.yml: configuração dos serviços.
- .gitignore: arquivos locais ignorados pelo Git.

## Status

- [x] Frontend funcional.
- [x] API FastAPI.
- [x] Integração frontend-backend.
- [x] Docker Compose.
- [x] Git e publicação no GitHub.
- [ ] Persistência com SQLite.
- [ ] Revisão com o agente de IA do Cursor.

## Contexto acadêmico

Laboratório Full Stack da UniCarioca.
