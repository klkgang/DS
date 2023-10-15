import sqlite3 as sql
from flask import Flask, request, jsonify

app = Flask(__name__)
conn = None

try:
    # Establecer conexión a la base de datos
    conn = sql.connect('database.db')
    print("Conexión exitosa a la base de datos!")
    cursor = conn.cursor()

    # Crear la tabla usuarios si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT
        )
    ''')
    conn.commit()

except sql.Error as e:
    print("Error al conectar a la base de datos:", e)

finally:
    if conn:
        conn.close()

@app.route('/endpoint', methods=['POST'])
def receive_data():
    data = request.get_json()
    print('Datos recibidos:', data)
    return jsonify({'message': 'Datos recibidos correctamente'})

if __name__ == '__main__':
    app.run()

