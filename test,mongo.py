import psycopg2
import pandas as pd

def connect_postgres(dbname, password, host, port):
    conn = psycopg2.connect(
        dbname=dbname,
        password=password,
        host=host,
        port=port
    )
    return conn

def query_postgres(conn, query):
    df = pd.read_sql_query(query, conn)
    return df
