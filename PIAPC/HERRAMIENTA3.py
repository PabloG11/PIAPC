try:
    import requests
    import io
    import csv
    import traceback
    from PIL import Image
    from bs4 import BeautifulSoup

    # URL de la página web de la UANL
    url = 'https://www.uanl.mx'

    # Nombre del archivo CSV para guardar los resultados
    csv_filename = 'metadatos_imagenes.csv'

    # Realizar la solicitud HTTP GET
    response = requests.get(url)

    # Comprobar el estado de la respuesta
    if response.status_code == 200:
        # Crear el objeto BeautifulSoup con el contenido HTML de la respuesta
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar las etiquetas de imagen en la página
        imagenes = soup.find_all('img')

        # Lista para almacenar los datos de los metadatos
        datos_metadatos = []

        # Procesar las imágenes
        for imagen in imagenes:
            # Obtener la URL de la imagen
            imagen_url = imagen['src']

            # Realizar la solicitud HTTP GET de la imagen
            imagen_response = requests.get(imagen_url)

            # Verificar si la solicitud de la imagen fue exitosa
            if imagen_response.status_code == 200:
                # Leer los datos de la imagen
                imagen_data = io.BytesIO(imagen_response.content)

                # Abrir la imagen utilizando Pillow
                img = Image.open(imagen_data)

                # Verificar si la imagen tiene metadatos
                if img.info:
                    datos_metadatos.append({
                        'URL': imagen_url,
                        'Metadatos': img.info
                    })

            else:
                print(f'No se pudo obtener la imagen {imagen_url}: {imagen_response.status_code}')

        # Guardar los datos de los metadatos en un archivo CSV
        with open(csv_filename, 'w', newline='') as csv_file:
            fieldnames = ['URL', 'Metadatos']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(datos_metadatos)

        print(f'Los metadatos se han guardado en el archivo {csv_filename}.')

    else:
        print('No se pudo obtener la página:', response.status_code)
except:
    with open("logs.txt", "a") as logfile:
            traceback.print_exc(file=logfile)
            raise
        
