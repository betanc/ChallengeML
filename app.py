from fastapi import FastAPI
import psycopg2

app = FastAPI()

# Conexion a la base de datos
conn = psycopg2.connect(
    host="db",
    port="5432",
    user="diegomb",
    password="DDD111+",
    database="clientes"
)


@app.get("/users")
def get_usuarios():
    cursor = conn.cursor()

    # Consulta a la base de datos
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # JSON
    consulta = []
    for row in rows:
        resp = {
            'id': row[0],
            'user_name': row[1],
            'fec_alta': row[2],
            'codigo_zip': row[3],
            'cuenta_numero': row[4],
            'direccion': row[5],
            'geo_latitud': row[6],
            'geo_longitud': row[7],
            'color_favorito': row[8],
            'foto_dni': row[9],
            'ip': row[10],
            'auto': row[11],
            'auto_modelo': row[12],
            'auto_tipo': row[13],
            'auto_color': row[14],
            'cantidad_compras_realizadas': row[15],
            'avatar': row[16],
            'fec_birthday': row[17],
        }
        consulta.append(resp)

    cursor.close()

    return consulta


@app.get("/tarjetas")
def get_tarjetas():
    cursor = conn.cursor()

    # Consulta a la tabla "credit_cards"
    cursor.execute("SELECT * FROM credit_cards")
    rows = cursor.fetchall()

    # JSON
    consulta = []
    for row in rows:
        resp = {
            'id': row[0],
            'cuenta_numero': row[1],
            'user_id': row[2],
            'credit_card_num': row[3],
            'credit_card_ccv': row[4],
        }
        consulta.append(resp)

    cursor.close()

    return consulta

"""
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

    """