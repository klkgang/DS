import sqlite3 as sql
from flask import Flask, request, jsonify

try:
    sofi = sql.connect('database.db')
    print ("Conexion exitosa a la base de datos!!")

except FileNotFoundError:
    print("No se podido encontrar la base datos")

cursor = sofi.cursor

mensaje = ("""
CREATE TABLE usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT.                                     
);""")

cursor.execute(mensaje)
sofi.commit()
sofi.close