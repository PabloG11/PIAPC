import subprocess, sys
import argparse

def mostrar_menu(opciones):
    print('\nSeleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Herramienta 1: Esta herramienta básicamente lo que hace es hacer un escaneo de todo el equipo y lo que hace es mandar toda esa información a un correo dado en el archivo de powershell, obviamente se tienen que ingresar el correo destinatario, el correo remitente (también su contraseña), el asunto, entre otras cosas; antes de ejecutar el script. Es importante saber que si no se conceden estos parametros dentro del script ps1, no funcionará el script.\n', accion1),
        
        '2': ('Herramienta 2: Esta herramienta realiza un escaneo de puertos del equipo y mandará en pantalla el # de puerto abierto y la leyenda "Puerto #0 Está abierto". Para el funcionamiento de este script el usuario deberá ejecutar el script como un script de python y tendrá que darle parametros, los parametros son la ip del equipo y el rango de puertos que se desea escanear.\n', accion2),
        '3': ('Herramienta 3: Esta herramienta lo que hace es un webscraping de imagenes de una pagina web dada, en este ejemplo pusimos la pagina de la uanl y recopila las imagenes, posteriormente saca las imagenes que contengan metadate y los guarda en un archivo .csv.\n', accion3),
        '4': ('Herramienta 4: Esta herramienta lo que hace es encriptar contraseñas y guardarlas en un archivo .csv ya encriptadas.\n', accion4),
        '5': ('Herramienta 5: Esta herramienta realiza la decodificación de las contraseñas encriptadas guardadas en el archivo .csv.\n', accion5),
        '6': ('Salir', salir)
    }

    generar_menu(opciones, '6')


def accion1():
     p = subprocess.Popen(["powershell.exe", "C:\\Users\elcha\Desktop\PIAPC\HERRAMIENTA1.py"], stdout=sys.stdout)
     p.communicate()
     
    

def accion2():
    dirip = input("Introduzca la direccion ip de su equipo: ")
    rangopuertos = input("Introduzca el rango de puertos en un formato #-#: ",)
    ruta ="C:\\Users\elcha\Desktop\PIAPC\HERRAMIENTA2.py " + dirip + " " + rangopuertos
    p = subprocess.Popen(["powershell.exe", ruta], stdout=sys.stdout)
    p.communicate()


def accion3():
    p = subprocess.Popen(["powershell.exe", "C:\\Users\elcha\Desktop\PIAPC\HERRAMIENTA3.py"], stdout=sys.stdout)
    p.communicate()
    

def accion4():
    p = subprocess.Popen(["powershell.exe", "C:\\Users\elcha\Desktop\PIAPC\HERRAMIENTA4.py"], stdout=sys.stdout)
    p.communicate()
    

def accion5():
    p = subprocess.Popen(["powershell.exe", "C:\\Users\elcha\Desktop\PIAPC\HERRAMIENTA5.py"], stdout=sys.stdout)
    p.communicate()
    
    
def salir():
    print('Saliendo')

class FooAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            accion1()
class FooAction2(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            accion2()
class FooAction3(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            accion3()
class FooAction4(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            accion4()
class FooAction5(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            accion5()





if __name__ =='__main__':
    
   
    parser = argparse.ArgumentParser()
    parser.add_argument('-a1', '--a1', action=FooAction, nargs='?', type=int, const=1, help='Esta herramienta básicamente lo que hace es hacer un escaneo de todo el equipo y lo que hace es mandar toda esa información a un correo dado en el archivo de powershell, obviamente se tienen que ingresar el correo destinatario, el correo remitente (también su contraseña), el asunto, entre otras cosas; antes de ejecutar el script. Es importante saber que si no se conceden estos parametros dentro de este script ps1, no funcionará el script.')
    

    parser.add_argument('-a2', '--a2', action=FooAction2, nargs='?', type=int, const=2, help='Esta herramienta necesita 2 parametros de entrada, la dirección ip y el rango de puertos deseados a escanear en formato #-#')
    

    parser.add_argument('-a3', '--a3', action=FooAction3, nargs='?', type=int, const=3, help='Esta herramienta lo que hace es un webscraping de imagenes de una pagina web dada, en este ejemplo pusimos la pagina de la uanl y recopila las imagenes, posteriormente saca las imagenes que contengan metadate y los guarda en un archivo .csv.')
    

    parser.add_argument('-a4', '--a4', action=FooAction4, nargs='?', type=int, const=4, help='Esta herramienta lo que hace es encriptar contraseñas y guardarlas en un archivo .csv ya encriptadas.')
    

    parser.add_argument('-a5', '--a5', action=FooAction5, nargs='?', type=int, const=5, help='Esta herramienta realiza la decodificación de las contraseñas encriptadas guardadas en el archivo .csv.')
    results = parser.parse_args(sys.argv[1:])

    menu_principal() 

    

    
    
