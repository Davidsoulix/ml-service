import os
from dotenv import load_dotenv
import psycopg2

# Cargar variables desde .env
load_dotenv()

# Configuración de la base de datos
DB_HOST = os.getenv("DB_HOST", "host.docker.internal")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "swfinal")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "2405")

def conectar():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

def obtener_id_tipo_cliente(nombre_tipo):
    with conectar() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id_tipocliente FROM tipo_clientes WHERE nombre = %s", (nombre_tipo,))
            row = cur.fetchone()
            return row[0] if row else None

def obtener_id_cliente(email):
    with conectar() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id_cliente FROM clientes WHERE email = %s", (email,))
            row = cur.fetchone()
            return row[0] if row else None

def crear_cliente(nombre, empresa, email):
    with conectar() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO clientes (nombre, empresa, email, id_sector)
                VALUES (%s, %s, %s, 1)
                RETURNING id_cliente
            """, (nombre, empresa, email))
            conn.commit()
            return cur.fetchone()[0]

def crear_solicitud(descripcion, id_cliente, id_tipo):
    with conectar() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO solicituds (descripcion, id_cliente, id_tipocliente)
                VALUES (%s, %s, %s)
            """, (descripcion, id_cliente, id_tipo))
            conn.commit()
