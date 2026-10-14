from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Full Stack UniCarioca",
    description="API inicial do laboratório Full Stack.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "API Full Stack UniCarioca funcionando"}


@app.get("/projects")
def list_projects():
    return {
        "projects": [
            {
                "id": 1,
                "name": "Laboratório Full Stack UniCarioca",
                "status": "em desenvolvimento",
            }
        ]
    }
