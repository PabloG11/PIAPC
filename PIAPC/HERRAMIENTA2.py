try:
#Parte1
#Importamos librerías necesarias
    import sys
    import threading
    import time
    import traceback
    from socket import *


    
    #Parte2
    #Creamos una función tcp_test la cual
    #permite probar mediante socket los puertos
    #abiertos, se le agrega lock.release()
    def tcp_test(port):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(10)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print("Puerto abierto: " , port)
            time.sleep(5)

    #Parte3
    #Establecemos el main del script
    #Guardamos en variables host y portstrs
    if __name__=='__main__':
        #HERRAMIENTA2 198. 1-8000
        host = sys.argv[1]
        portstrs = sys.argv[2].split('-')

        #Parte4
        #portstrs se convierte en lista al momento
        #de hacer split y de ahí obtener dos valores
        start_port = int(portstrs[0])
        end_port = int(portstrs[1])

        #Parte5
        #Usando la funcion gethostbyname se obtiene
        #la dirección ip.
        target_ip = gethostbyname(host)

        #Parte6
        #se inicia bucle para probar puertos
        #usando la función tcp_test y generando
        #un hilo por cada puerto a probar
        hilos = []
        for port in range(start_port, end_port):
            hilo = threading.Thread(target=tcp_test, args=(port,))
            hilos.append(hilo)
            hilo.start()
except:
    with open("logs.txt", "a") as logfile:
            traceback.print_exc(file=logfile)
            raise
