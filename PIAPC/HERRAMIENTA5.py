try:
    import traceback
    import base64
    import csv
    import time

    def decodificar_base64(texto_codificado):
        # Decodificar el texto Base64
        texto_decodificado = base64.b64decode(texto_codificado).decode()
        return texto_decodificado

    # Nombre del archivo CSV que contiene las contraseñas
    csv_filename = 'contraseñas.csv'

    # Leer las contraseñas almacenadas en el archivo CSV
    contraseñas = []
    with open(csv_filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            contraseña_codificada = row[0]
            contraseña_decodificada = decodificar_base64(contraseña_codificada)
            contraseñas.append(contraseña_decodificada)

    # Imprimir las contraseñas decodificadas
    print('Contraseñas decodificadas:')
    for contraseña in contraseñas:
        print(contraseña)
        time.sleep(10)
        
except:
    with open("logs.txt", "a") as logfile:
            traceback.print_exc(file=logfile)
            raise
