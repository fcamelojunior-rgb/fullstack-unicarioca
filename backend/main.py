
import os
import sqlite3
from contextlib import closing

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

DATABASE_PATH = os.getenv("DATABASE_PATH", "/data/projects.db")

app = FastAPI(
    title="Full Stack UniCarioca",
    description="API Full Stack com persistência em SQLite.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


def initialize_database():
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)

    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                status TEXT NOT NULL
            )
            """
        )

        connection.execute(
            """
            INSERT INTO projects (name, status)
            SELECT ?, ?
            WHERE NOT EXISTS (SELECT 1 FROM projects)
            """,
            ("Laboratório Full Stack UniCarioca", "em desenvolvimento"),
        )

        connection.commit()


@app.on_event("startup")
def startup():
    initialize_database()


@app.get("/")
def home():
    return {"message": "API Full Stack UniCarioca funcionando"}


@app.get("/projects")
def list_projects():
    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            "SELECT id, name, status FROM projects ORDER BY id"
        ).fetchall()

    return {"projects": [dict(row) for row in rows]}
