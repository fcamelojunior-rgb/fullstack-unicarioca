# Laboratório Full Stack UniCarioca

Projeto acadêmico de Ciência da Computação desenvolvido no Laboratório Full Stack da UniCarioca.

O **Painel de Demandas e Ações** é uma aplicação web que permite registrar, consultar, editar e excluir demandas, além de acompanhar indicadores por status.

## Funcionalidades

- Cadastro de novas demandas.
- Listagem das demandas registradas.
- Edição de demandas existentes.
- Exclusão de demandas com confirmação.
- Resumo quantitativo por status.
- Persistência de dados em banco SQLite.
- API REST documentada com FastAPI.

## Tecnologias utilizadas

| Camada | Tecnologias |
|---|---|
| Frontend | HTML, CSS e JavaScript |
| Servidor web | Nginx |
| Backend | Python, FastAPI e Uvicorn |
| Banco de dados | SQLite |
| Contêineres | Docker e Docker Compose |
| Controle de versão | Git |

## Arquitetura

O frontend é servido pelo Nginx na porta 8080. O JavaScript envia requisições HTTP para a API FastAPI, disponibilizada na porta 8000. O backend valida os dados e realiza as operações no banco SQLite.

O volume Docker `sqlite_data` mantém os dados persistidos entre reinicializações dos contêineres.

A tabela `projects`, utilizada na etapa anterior, é preservada. A tabela `demands` armazena os registros do painel.

Para mais detalhes, consulte [ARCHITECTURE.md](ARCHITECTURE.md).

## Endereços locais

| Recurso | Endereço |
|---|---|
| Interface web | http://localhost:8080 |
| API | http://localhost:8000 |
| Documentação interativa da API | http://localhost:8000/docs |
| Verificação de saúde | http://localhost:8000/health |
| Listagem de demandas | http://localhost:8000/demands |
| Indicadores | http://localhost:8000/summary |

## Como executar

Pré-requisitos: Docker Desktop instalado e em execução, com suporte ao WSL habilitado.

Na raiz do repositório, execute:

```bash
docker compose up -d --build
```

Verifique o estado dos contêineres:

```bash
docker compose ps
```

Abra http://localhost:8080 no navegador.

Para consultar a documentação e testar os endpoints da API, abra http://localhost:8000/docs.

Para parar os contêineres sem remover os dados persistidos:

```bash
docker compose stop
```

**Importante:** evite `docker compose down -v` quando precisar preservar o volume `sqlite_data`, pois esse comando remove os volumes declarados no Compose.

## Estrutura do projeto

```text
.
├── backend/
│   ├── app/
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── schemas.py
│   │   └── services.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── app.js
│   ├── index.html
│   └── style.css
├── ARCHITECTURE.md
├── AGENTS.md
├── docker-compose.yml
└── README.md
```

## Endpoints principais

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/health` | Verifica a disponibilidade da API |
| GET | `/projects` | Consulta os projetos da etapa anterior |
| GET | `/demands` | Lista demandas |
| POST | `/demands` | Cadastra uma demanda |
| PUT | `/demands/{demand_id}` | Atualiza uma demanda |
| DELETE | `/demands/{demand_id}` | Exclui uma demanda |
| GET | `/summary` | Retorna os indicadores |

## Validação funcional

Os testes realizados incluem:

- Consulta do estado de saúde da API.
- Listagem de demandas e consulta de indicadores.
- Cadastro, edição e exclusão de uma demanda de teste pela interface.
- Verificação de que os registros originais permanecem preservados.

## Orientações para desenvolvimento

Consulte `AGENTS.md` para conhecer as orientações de manutenção e validação do projeto.
