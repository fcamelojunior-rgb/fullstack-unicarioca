# Arquitetura do Painel de Demandas e Ações

## 1. Visão geral

Aplicação web desenvolvida no Laboratório Full Stack da UniCarioca. O sistema permite cadastrar, consultar, editar e excluir demandas, além de apresentar indicadores quantitativos.

Tecnologias utilizadas: HTML, CSS, JavaScript, Python, FastAPI, SQLite, Docker e Docker Compose.

## 2. Componentes

### Frontend

Localização: `frontend/`

- `index.html`: estrutura da página, formulário, indicadores e listagem.
- `style.css`: estilos visuais e adaptação a diferentes telas.
- `app.js`: comunicação com a API e operações de cadastro, edição e exclusão.

O Nginx disponibiliza a interface na porta 8080.

### Backend

Localização: `backend/app/`

- `main.py`: aplicação FastAPI e rotas HTTP.
- `database.py`: conexão com SQLite e operações de persistência.
- `schemas.py`: modelos de dados utilizados na validação das requisições.
- `services.py`: funções auxiliares para tratamento de status e consulta de demandas.

O Uvicorn executa a API na porta 8000.

### Banco de dados

O SQLite armazena os dados. A variável `DATABASE_PATH` define o caminho do arquivo e, no Docker Compose, utiliza `/data/projects.db`.

O volume Docker `sqlite_data` preserva o banco entre reinicializações dos contêineres.

A tabela `projects`, da etapa anterior, é preservada. A tabela `demands` armazena as demandas do painel.

## 3. Fluxo de funcionamento

1. O usuário acessa a interface pelo navegador.
2. O JavaScript envia requisições HTTP à API.
3. A API valida os dados recebidos.
4. O backend consulta ou modifica o banco SQLite.
5. A API retorna os resultados em JSON.
6. A interface atualiza a listagem e os indicadores.

## 4. Endpoints da API

| Método | Endpoint | Finalidade |
|---|---|---|
| GET | `/health` | Verificar a disponibilidade da API |
| GET | `/projects` | Consultar projetos existentes |
| GET | `/demands` | Listar demandas |
| POST | `/demands` | Cadastrar uma demanda |
| PUT | `/demands/{demand_id}` | Atualizar uma demanda |
| DELETE | `/demands/{demand_id}` | Excluir uma demanda |
| GET | `/summary` | Consultar indicadores |
| GET | `/docs` | Abrir a documentação interativa |

## 5. Status das demandas

O sistema utiliza três status:

- `pendente`
- `em andamento`
- `concluída`

Os indicadores mostram o total de demandas e a quantidade em cada status.

## 6. Como executar

Na raiz do projeto, execute:

```bash
docker compose up -d --build
```

Acesse os endereços:

- Interface: http://localhost:8080
- API: http://localhost:8000
- Documentação da API: http://localhost:8000/docs
- Verificação de saúde: http://localhost:8000/health

Para parar os contêineres sem remover os dados:

```bash
docker compose stop
```

**Atenção:** não utilize `docker compose down -v` se precisar preservar o volume e os dados do banco.

## 7. Testes funcionais

A validação deve incluir:

- Verificação de saúde da API.
- Listagem das demandas.
- Consulta dos indicadores.
- Cadastro de uma demanda de teste.
- Edição da demanda.
- Exclusão da demanda de teste.
- Confirmação da preservação dos registros anteriores.
