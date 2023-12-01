import pyodbc

# Reemplaza 'tu_cadena_de_conexion' con tu cadena de conexión real
conn_str = 'Driver={ODBC Driver 17 for SQL Server};Server=tcp:newsmg.database.windows.net,1433;Database=Prueba;Uid=PedroSaray;Pwd={1Admin1!};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

#
# Intenta establecer la conexión
try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Ejemplo: Consulta SQL
    cursor.execute("SELECT TOP (200) firstName FROM [SalesLT].[Customer]")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

except pyodbc.Error as e:
    print(f"Error de conexión: {e}")

finally:
    # Cierra la conexión al finalizar
    if conn:
        conn.close()