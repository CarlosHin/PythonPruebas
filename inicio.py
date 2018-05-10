import sqlite3
def imprimirUsuarios():
    cont = 1
    print()
    for x in c.execute('''select * from usuarios'''):
        print("Nombre {cont}: {nombre} {apellido}".format(cont = cont, nombre=x[0], apellido=x[1]))
        cont +=1

conn =sqlite3.connect("Tabla de usuarios")
c = conn.cursor()
#c.execute('''drop table usuarios''')

try:
    c.execute('''create table usuarios (nombre text,apellido text)''')
except Exception:
    print("YA ESTÁ CREADA LA BASE DE DATOS")

nombre = input("Nombre: ")
apellido = input("Apellido: ")

c.execute('''insert into usuarios values('{nombre}', '{apellido}')'''.format(**locals()))



imprimirUsuarios()
c.close
conn.commit();
