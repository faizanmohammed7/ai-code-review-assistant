import sqlite3
import os

DB_PATH = "scans.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            repo TEXT,
            pr_number INTEGER,
            rule TEXT,
            file TEXT,
            line INTEGER,
            matched TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_finding(repo, pr_number, finding):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO scans (repo, pr_number, rule, file, line, matched) VALUES (?, ?, ?, ?, ?, ?)",
        (repo, pr_number, finding["rule"], finding["file"], finding["line"], finding["matched"])
    )
    conn.commit()
    conn.close()

def get_recent_scans(limit=20):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT repo, pr_number, rule, file, line, matched, timestamp FROM scans ORDER BY id DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()
    return rows