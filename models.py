import pymysql
from config import db

class Usuario:

    def create(name,username,password):
        conn = db()
        cur = conn.cursor()
        cur.execute("INSERT INTO usuario (nombre,usuario,contraseña) VALUES (%s,%s,%s)",(name,username,password))
        conn.commit()
        cur.close()
        conn.close()


    def login(username,password):
        conn = db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM usuario WHERE usuario=%s AND contraseña=%s",(username,password))
        resultado = cur.fetchone()
        if resultado:
            return True
        else:
            return False    
        

    
    def get_usuario(username,password):
        conn = db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM usuario WHERE usuario=%s AND contraseña=%s",(username,password))
        resultado = cur.fetchone()
        if resultado:
            return resultado
        else:
            return False
        
    def get_user(id):
        conn = db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM usuario WHERE id=%s",(id))
        resultado = cur.fetchone()
        if resultado:
            return resultado
        else:
            return False    


class producido:

    def create(nombre,reporte_dia,dia):
        conn = db()
        cur = conn.cursor()
        cur.execute("INSERT INTO producido_dia (usuario,produ_dia,fecha) VALUES (%s,%s,%s)",(nombre,reporte_dia,dia))
        conn.commit()
        cur.close()
        conn.close()


    def get_produccion():
        conn = db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM producido_dia")
        resultado = cur.fetchall()
        if resultado:
            return resultado
        else:
            return False
        

