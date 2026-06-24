import sqlite3

DB_NAME = "ideas.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ideas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        startup_name TEXT,
        industry TEXT,
        problem TEXT,
        solution TEXT,
        target_audience TEXT,
        revenue_model TEXT,
        market_score INTEGER
    )
    """)

    conn.commit()
    conn.close()


def save_idea(
    startup_name,
    industry,
    problem,
    solution,
    target_audience,
    revenue_model,
    market_score
):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO ideas
    (
        startup_name,
        industry,
        problem,
        solution,
        target_audience,
        revenue_model,
        market_score
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        startup_name,
        industry,
        problem,
        solution,
        target_audience,
        revenue_model,
        market_score
    ))

    conn.commit()
    conn.close()


def get_all_ideas():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ideas ORDER BY id DESC")

    ideas = cursor.fetchall()

    conn.close()

    return ideas