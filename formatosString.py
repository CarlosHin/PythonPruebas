
lista = [("nombre","Carlos"),("apellido","Hinojosa")]
dic = dict(lista)
a =19
print("Hola me llamo {0[nombre]} {0[apellido]}".format(dic))
print("Tengo {a} años".format(dic,**locals()))
