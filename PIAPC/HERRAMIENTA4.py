try:
    import traceback
    import base64
    import csv
    import getpass

    def codificar_base64(texto):
        # Codificar el texto a Base64
        texto_codificado = base64.b64encode(texto.encode()).decode()
        return texto_codificado

    # Obtener una contraseña del usuario de forma segura
    password = getpass.getpass('Ingrese la contraseña: ')

    # Codificar la contraseña a Base64
    password_codificada = codificar_base64(password)

    # Nombre del archivo CSV para guardar las contraseñas
    csv_filename = 'contraseñas.csv'

    # Guardar la contraseña codificada en el archivo CSV
    with open(csv_filename, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([password_codificada])

    print('La contraseña se ha guardado en el archivo', csv_filename)
except:
    with open("logs.txt", "a") as logfile:
            traceback.print_exc(file=logfile)
            raise
