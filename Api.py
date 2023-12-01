from flask import Flask, jsonify
from dotenv import load_dotenv
from decouple import config  # Importa la función 'config' de python-decouple
load_dotenv()

import pyodbc

app = Flask(__name__)

# cadena de conexión
conn_str = f'Driver={config("DB_DRIVER")};Server={config("DB_SERVER")};Database={config("DB_DATABASE")};Uid={config("DB_USER")};Pwd={config("DB_PASSWORD")};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

# Ruta para obtener datos desde la base de datos
@app.route('/api/clientes', methods=['GET'])
def obtener_clientes():
    try:
        # Intenta establecer la conexión
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Ejecuta una consulta SQL
        cursor.execute("SELECT TOP (200) firstName FROM [SalesLT].[Customer]")
        rows = cursor.fetchall()

        # Formatea los resultados en un JSON
        resultados = [{'firstName': row[0]} for row in rows]

        return jsonify({'clientes': resultados})

    except pyodbc.Error as e:
        return jsonify({'error': f"Error de conexión: {e}"}), 500

    finally:
        # Cierra la conexión al finalizar
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
