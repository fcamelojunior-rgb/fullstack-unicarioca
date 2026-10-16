from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.database import (
    init_db,
    list_projects,
    list_demands,
    get_demand_by_id,
    create_demand,
    update_demand,
    delete_demand,
)
from app.schemas import DemandCreate, DemandUpdate
from app.services import build_summary, normalize_status, list_all_demands


app = FastAPI(
    title="Painel de Demandas e Ações API",
    description="API da base comum do projeto de extensão",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    init_db()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/projects")
def get_projects():
    return {"projects": list_projects()}


@app.get("/demands")
def get_demands():
    return {"demands": list_all_demands()}


@app.get("/summary")
def get_demand_summary():
    return build_summary()


@app.post("/demands")
def post_demand(demand: DemandCreate):
    data = demand.model_dump()
    data["status"] = normalize_status(data["status"])
    created = create_demand(data)

    return {
        "message": "Demanda criada com sucesso",
        "demand": created,
    }


@app.put("/demands/{demand_id}")
def put_demand(demand_id: int, demand: DemandUpdate):
    if get_demand_by_id(demand_id) is None:
        raise HTTPException(status_code=404, detail="Demanda não encontrada")

    data = demand.model_dump()
    data["status"] = normalize_status(data["status"])
    updated = update_demand(demand_id, data)

    return {
        "message": "Demanda atualizada com sucesso",
        "demand": updated,
    }


@app.delete("/demands/{demand_id}")
def remove_demand(demand_id: int):
    if not delete_demand(demand_id):
        raise HTTPException(status_code=404, detail="Demanda não encontrada")

    return {"message": "Demanda excluída com sucesso"}
