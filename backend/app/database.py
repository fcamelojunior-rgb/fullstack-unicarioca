
from pathlib import Path
import os
import sqlite3

DB_PATH = Path(os.getenv("DATABASE_PATH", "/data/projects.db"))


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL DEFAULT 'Geral',
                status TEXT NOT NULL
            )
            """
        )

        columns = {
            row["name"]
            for row in connection.execute("PRAGMA table_info(projects)")
        }

        if "category" not in columns:
            connection.execute(
                "ALTER TABLE projects ADD COLUMN category TEXT NOT NULL DEFAULT 'Geral'"
            )

        examples = [
            ("Painel de Ações da ONG", "ONG", "Preparação"),
            ("Agenda Digital da Escola", "Educação", "Estrutura inicial"),
        ]

        for name, category, status in examples:
            connection.execute(
                """
                INSERT INTO projects (name, category, status)
                SELECT ?, ?, ?
                WHERE NOT EXISTS (
                    SELECT 1 FROM projects WHERE name = ?
                )
                """,
                (name, category, status, name),
            )


def list_projects():
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT id, name, category, status FROM projects ORDER BY id"
        ).fetchall()

        return [dict(row) for row in rows]
