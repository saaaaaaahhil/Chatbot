import psycopg2
import pandas as pd

def connect_postgres(dbname, user, password, host, port):
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    return conn

def query_postgres(conn, query):
    df = pd.read_sql_query(query, conn)
    return df
