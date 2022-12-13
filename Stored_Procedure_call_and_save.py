# este script en python se conecta a una base de datos ejecuta un stored procedurte y guarda un archivo txt con el resultado
import pyodbc
import datetime

# Configuramos la cadena de conexión a la base de datos
connection_string = "DRIVER={SQL Server};SERVER=nombre_del_servidor;DATABASE=nombre_de_la_base_de_datos;UID=usuario;PWD=contraseña"

# Establecemos la conexión a la base de datos
cnxn = pyodbc.connect(connection_string)

# Creamos un cursor para realizar la consulta
cursor = cnxn.cursor()

# Ejecutamos el Stored Procedure "get_data"
cursor.execute("EXEC get_data")

# Obtenemos el resultado de la consulta
result = cursor.fetchall()

# Cerramos el cursor
cursor.close()

# Obtenemos la hora actual
current_time = datetime.datetime.now()

# Creamos un archivo .txt con el nombre de la hora actual
file_name = current_time.strftime("%H%M%S") + ".txt"
file = open(file_name, "w")

# Recorremos el resultado de la consulta y escribimos cada fila en el archivo .txt
for row in result:
    file.write(str(row) + "\n")

# Cerramos el archivo
file.close()
