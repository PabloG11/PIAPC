# PIAPC
Herramientas de ciberseguridad
Herramienta 1: Esta herramienta básicamente lo que hace es hacer un escaneo de todo el equipo y lo que hace es mandar toda esa información a un correo dado en el archivo de powershell, obviamente se tienen que ingresar el correo destinatario, el correo remitente (también su contraseña), el asunto, entre otras cosas; antes de ejecutar el script. Es importante saber que si no se conceden estos parametros dentro del script ps1, no funcionará el script.
Herramienta 2: Esta herramienta realiza un escaneo de puertos del equipo y mandará en pantalla el # de puerto abierto y la leyenda "Puerto #0 Está abierto". Para el funcionamiento de este script el usuario deberá ejecutar el script como un script de python y tendrá que darle parametros, los parametros son la ip del equipo y el rango de puertos que se desea escanear.
Herramienta 3: Esta herramienta lo que hace es un webscraping de imagenes de una pagina web dada, en este ejemplo pusimos la pagina de la uanl y recopila las imagenes, posteriormente saca las imagenes que contengan metadate y los guarda en un archivo .csv.
Herramienta 4: Esta herramienta lo que hace es encriptar contraseñas y guardarlas en un archivo .csv ya encriptadas.
Herramienta 5: Esta herramienta realiza la decodificación de las contraseñas encriptadas guardadas en el archivo .csv.
