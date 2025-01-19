import datetime
from flask import Flask, render_template, request, redirect, session
from config import db
from models import Usuario, producido  # Asegúrate de que config.py tenga db configurado
import os

app = Flask(__name__)  # Crea la aplicación Flask
app.secret_key = os.urandom(24)  # Genera una clave secreta segura

# Rutas
@app.route('/')
def login():
    return render_template('login.html')  # Renderiza la plantilla login.html

@app.route('/logout')
def logout():
    session.clear()  # Limpia la sesión
    return render_template('logout.html')

@app.route('/index')
def index():
    if 'user_id' not in session:
        return redirect('/')
    
    user = Usuario.get_user(session['user_id'])
    if not user:
        return redirect('/')
    
    nombre, usuario_name = user[1], user[2]
    rows = producido.get_produccion()
    print(session)
    return render_template('index.html', rows=rows, nombre=nombre, usuario_name=usuario_name)

@app.route('/logout_post', methods=['POST'])
def logout_post():
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    
    Usuario.create(name, username, password)
    return render_template('login.html')

@app.route('/login_post', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    usuario = Usuario.get_usuario(username, password)
    if usuario:
        session['user_id'] = usuario[0] 
        session['nombre'] = usuario[1]
        session['usuario_name'] = usuario[2]

        return redirect('/index')
    else:
        return render_template('login.html', error="Usuario o contraseña incorrectos")

@app.route('/register_dia', methods=['POST'])
def register_dia():
    if 'user_id' not in session:
        return redirect('/')
    
    name = request.form['nombre']
    reporte_dia = request.form['reporte_dia']
    fecha = datetime.datetime.now().date()
    producido.create(name, reporte_dia, fecha)

    return redirect('/index')

if __name__ == '__main__':
    app.run(debug=True)  # Inicia la aplicación
