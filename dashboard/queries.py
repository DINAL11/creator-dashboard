import sqlite3
import pandas as pd

DB_PATH = "data/creator_data.db"

def run_query(query: str) -> pd.DataFrame:
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def get_key_metrics():
    return run_query("""
        SELECT 
            COUNT(DISTINCT creator) AS total_creators,
            SUM(views) AS total_views,
            SUM(likes) AS total_likes,
            SUM(comments) AS total_comments,
            ROUND(SUM(revenue), 2) AS total_revenue
        FROM creator_metrics;
    """)

def get_time_series():
    return run_query("""
        SELECT 
            date,
            SUM(views) as views,
            SUM(likes) as likes,
            SUM(comments) as comments,
            SUM(revenue) as revenue
        FROM creator_metrics
        GROUP BY date
        ORDER BY date;
    """)
