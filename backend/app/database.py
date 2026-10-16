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
        # Preserva a tabela da Etapa 1.
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

        # Nova tabela da Etapa 2.
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS demands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL,
                status TEXT NOT NULL,
                owner TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )

        total = connection.execute(
            "SELECT COUNT(*) FROM demands"
        ).fetchone()[0]

        # Insere exemplos somente se a tabela estiver vazia.
        if total == 0:
            examples = [
                (
                    "Organizar evento comunitário",
                    "Comunidade",
                    "Planejar local, divulgação e equipe de apoio",
                    "pendente",
                    "Marina",
                    "2026-04-11",
                ),
                (
                    "Cadastrar voluntários",
                    "ONG",
                    "Registrar nome, contato e área de interesse",
                    "em andamento",
                    "Carlos",
                    "2026-04-11",
                ),
                (
                    "Atualizar agenda escolar",
                    "Educação",
                    "Publicar calendário com atividades do mês",
                    "concluída",
                    "Luciana",
                    "2026-04-11",
                ),
            ]

            connection.executemany(
                """
                INSERT INTO demands
                    (title, category, description, status, owner, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                examples,
            )


def list_demands():
    with get_connection() as connection:
        rows = connection.execute(
            """
            SELECT id, title, category, description, status, owner, created_at
            FROM demands
            ORDER BY id
            """
        ).fetchall()

        return [dict(row) for row in rows]


def get_demand_by_id(demand_id: int):
    with get_connection() as connection:
        row = connection.execute(
            """
            SELECT id, title, category, description, status, owner, created_at
            FROM demands
            WHERE id = ?
            """,
            (demand_id,),
        ).fetchone()

        return dict(row) if row else None


def create_demand(demand: dict):
    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO demands
                (title, category, description, status, owner, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                demand["title"],
                demand["category"],
                demand["description"],
                demand["status"],
                demand["owner"],
                demand["created_at"],
            ),
        )

        demand_id = cursor.lastrowid

    return get_demand_by_id(demand_id)


def update_demand(demand_id: int, demand: dict):
    with get_connection() as connection:
        cursor = connection.execute(
            """
            UPDATE demands
            SET title = ?, category = ?, description = ?,
                status = ?, owner = ?, created_at = ?
            WHERE id = ?
            """,
            (
                demand["title"],
                demand["category"],
                demand["description"],
                demand["status"],
                demand["owner"],
                demand["created_at"],
                demand_id,
            ),
        )

        updated = cursor.rowcount > 0

    return get_demand_by_id(demand_id) if updated else None


def delete_demand(demand_id: int):
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM demands WHERE id = ?",
            (demand_id,),
        )

        return cursor.rowcount > 0


def get_summary():
    with get_connection() as connection:
        total = connection.execute(
            "SELECT COUNT(*) FROM demands"
        ).fetchone()[0]

        pending = connection.execute(
            "SELECT COUNT(*) FROM demands WHERE status = 'pendente'"
        ).fetchone()[0]

        in_progress = connection.execute(
            "SELECT COUNT(*) FROM demands WHERE status = 'em andamento'"
        ).fetchone()[0]

        done = connection.execute(
            "SELECT COUNT(*) FROM demands WHERE status = 'concluída'"
        ).fetchone()[0]

        return {
            "total": total,
            "pending": pending,
            "in_progress": in_progress,
            "done": done,
        }
def list_projects():
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT id, name, category, status FROM projects ORDER BY id"
        ).fetchall()
        return [dict(row) for row in rows]
