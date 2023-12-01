from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

# Configuración de la cadena de conexión
conn_str = 'Driver={ODBC Driver 17 for SQL Server};Server=tcp:newsmg.database.windows.net,1433;Database=Prueba;Uid=PedroSaray;Pwd={1Admin1!};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

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
