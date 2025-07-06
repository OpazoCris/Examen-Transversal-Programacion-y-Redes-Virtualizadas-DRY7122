#ET C.opazo Fel.sobarzo
from flask import Flask, request, render_template_string
import sqlite3
import hashlib
import os

DB_NAME = "usuarios.db"

def crear_bd():
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                password_hash TEXT NOT NULL
            )
        """)
    
        usuarios = {
            "Cristopher Opazo": "clave123",
            "Felipe Sobarzo": "clave321",
        }
        for nombre, clave in usuarios.items():
            clave_hash = hashlib.sha256(clave.encode()).hexdigest()
            cursor.execute("INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)", (nombre, clave_hash))
        conn.commit()
        conn.close()

crear_bd()

app = Flask(__name__)

html = """
<!doctype html>
<title>DRY7122</title>
<h2>Examen Transversal DRY7122</h2>
<form method=post>
  Nombre: <input type=text name=nombre><br><br>
  Contraseña: <input type=password name=clave><br><br>
  <input type=submit value=Ingresar>
</form>
<p>{{ mensaje }}</p>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    mensaje = ''
    if request.method == 'POST':
        nombre = request.form['nombre']
        clave = request.form['clave']
        clave_hash = hashlib.sha256(clave.encode()).hexdigest()

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND password_hash=?", (nombre, clave_hash))
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            mensaje = f"Bienvenido, {nombre}."
        else:
            mensaje = "Usuario o contraseña incorrecta."
    return render_template_string(html, mensaje=mensaje)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7500)
