import pymysql

def db():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='tienda'
    )
    
