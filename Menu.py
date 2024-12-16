# Importa las librerías necesarias para conectar con las diferentes bases de datos
# import mysql.connector  # Descomentado si se usa MySQL
import sqlite3  # Conexión con SQLite
import mariadb  # Conexión con MariaDB
import psycopg  # Conexión con PostgreSQL
import psycopg_binary  # Biblioteca adicional para PostgreSQL
import sys  # Permite interactuar con el sistema, no se está usando en este código directamente


# Definición de la clase Menu que maneja el menú y las operaciones CRUD para las diferentes bases de datos
class Menu:
    def __init__(self):
        # Inicializa la conexión como None y un flag de ejecución
        self.conn = None
        self.ejecutar = True  # Variable que controla si el menú sigue activo



    def menu(self):
        # Función principal que despliega el menú y gestiona la interacción del usuario
        while self.ejecutar == True:
            # Imprime las opciones del menú
            print("\nMENU DE BASES DE DATOS")
            print("*************************")
            print("1- PostgreSQL")
            print("2- MariaDB")
            print("3- SQLite3")
            print("0- Salir")
            print("*************************")

            # Pide al usuario que ingrese una opción
            opc = input("\nIntroduzca alguna opcion: ")

            # Verifica si la opción es válida
            if opc in ["0", "1", "2", "3"]:
                if opc == "1":
                    print("\nBienvenido a PostgreSQL!")
                    self.crudPostgreSQL()  # Llama a la función para manejar PostgreSQL
                elif opc == "2":
                    print("\nBienvenido a MariaDB!")
                    self.crudMariaDB()  # Llama a la función para manejar MariaDB
                elif opc == "3":
                    print("\nBienvenido a SQLite3!")
                    self.crudSQLite3()  # Llama a la función para manejar SQLite3
                elif opc == "0":
                    print("Saliendo del programa")
                    self.ejecutar = False  # Cambia el flag de ejecución para salir del ciclo
                    exit()  # Sale del programa
            else:
                # Si la opción no es válida, se solicita al usuario ingresar una válida
                print("Ingrese una opcion válida")





    def crudPostgreSQL(self):
        # Función para interactuar con PostgreSQL
        print("\n*************************************************")
        print("1/20 Conectar con la base de datos PRESIONA ENTER")
        input()  # Espera que el usuario presione ENTER

        # Intenta conectarse a la base de datos PostgreSQL
        try:
            db = psycopg.connect(
                user="postgres",
                password="1234",
                host="localhost",
                port=5432,
                dbname="bdpython"
            )
            print("2/20 Te has conectado con exito PRESIONA ENTER")
            input()  # Espera que el usuario presione ENTER

        except psycopg.Error as e:
            # Si ocurre un error de conexión, lo muestra
            print(f"Error de conexion con la db PostgreSQL: {e}")

        print("3/20 Habilitar el cursor PRESIONA ENTER")
        input()  # Espera que el usuario presione ENTER
        cur = db.cursor()  # Crea un cursor para ejecutar consultas
        print("4/20 Cursor habilitado con exito PRESIONA ENTER")
        input()  # Espera que el usuario presione ENTER

        opc = 1  # Opción para PostgreSQL
        self.crud(db, cur, opc)  # Llama a la función CRUD pasando la conexión y cursor


    def crudMariaDB(self):
        # Función para interactuar con MariaDB
        print("\n*************************************************")
        print("1/20 Conectar con la base de datos PRESIONA ENTER")
        input()  # Espera que el usuario presione ENTER

        # Intenta conectarse a la base de datos MariaDB
        try:
            db = mariadb.connect(
                user="root",
                password="",
                host="localhost",
                port=3306,
                database="bdpython"
            )
            print("2/20 Te has conectado con exito PRESIONA ENTER")
            input()  # Espera que el usuario presione ENTER

        except mariadb.Error as e:
            # Si ocurre un error de conexión, lo muestra
            print(f"Error de conexion con la db MariaDB: {e}")

        print("3/20 Habilitar el cursor PRESIONA ENTER")
        input()  # Espera que el usuario presione ENTER
        cur = db.cursor()  # Crea un cursor para ejecutar consultas
        print("4/20 Cursor habilitado con exito PRESIONA ENTER")
        input()  # Espera que el usuario presione ENTER

        opc = 2  # Opción para MariaDB
        self.crud(db, cur, opc)  # Llama a la función CRUD pasando la conexión y cursor


    def crudSQLite3(self):
        # Función para interactuar con SQLite3
        print("\n*************************************************")
        print("1/20 Conectar con la base de datos PRESIONA ENTER")
        input()  # Espera que el usuario presione ENTER

        # Intenta conectarse a la base de datos SQLite
        bd = sqlite3.connect("SebastianExpositoRuiz.db")  # Conecta o crea el archivo SQLite
        print("2/20 Te has conectado con exito PRESIONA ENTER")
        input()  # Espera que el usuario presione ENTER

        print("3/20 Habilitar el cursor PRESIONA ENTER")
        input()  # Espera que el usuario presione ENTER
        cursor = bd.cursor()  # Crea un cursor para ejecutar consultas
        print("4/20 Cursor habilitado con exito PRESIONA ENTER")
        input()  # Espera que el usuario presione ENTER

        opc = 3  # Opción para SQLite3
        self.crud(bd, cursor, opc)  # Llama a la función CRUD pasando la conexión y cursor



    def crud(self, bd, cursor, opc):
        # Función genérica que maneja las operaciones CRUD
        try:
            print("\n************")
            print("    CRUD")
            print("************")

            print("\nCREAR")
            print("*************************************************")
            print("5/20 Crear tablas PRESIONA ENTER")
            input()  # Espera que el usuario presione ENTER

            # Elimina la tabla "SebastianExpositoRuiz" si existe para evitar conflictos
            cursor.execute("DROP TABLE IF EXISTS SebastianExpositoRuiz")
            bd.commit()  # Guarda los cambios

            # Dependiendo de la opción seleccionada, crea la tabla correspondiente
            if opc == 1 :
                # Crear tabla para PostgreSQL
                tablas = [
                    """
                        CREATE TABLE IF NOT EXISTS SebastianExpositoRuiz(
                            id TEXT PRIMARY KEY,                -- UUID nativo
                            nombre TEXT NOT NULL,               -- Nombre obligatorio
                            edad INTEGER CHECK (edad > 0),      -- Edad positiva
                            salario NUMERIC(10, 2),             -- Número decimal con precisión
                            es_genio BOOLEAN,                   -- Booleano nativo (TRUE o FALSE)
                            f_inicio DATE                       -- Fecha en formato DATE
                        );
                    """
                ]
            elif opc == 2:
                # Crear tabla para MariaDB
                tablas = [
                    """
                        CREATE TABLE IF NOT EXISTS SebastianExpositoRuiz(
                            id CHAR(36) PRIMARY KEY,            -- UUID como cadena de 36 caracteres
                            nombre VARCHAR(255) NOT NULL,       -- Nombre obligatorio
                            edad INT CHECK (edad > 0),          -- Edad positiva
                            salario DECIMAL(10, 2),             -- Número decimal con 2 decimales
                            es_genio BOOLEAN,                   -- Booleano nativo (TRUE o FALSE)
                            f_inicio DATE                       -- Fecha en formato DATE
                        );
                    """
                ]
            elif opc == 3:
                # Crear tabla para SQLite3
                tablas = [
                    """
                        CREATE TABLE IF NOT EXISTS SebastianExpositoRuiz(
                            id TEXT PRIMARY KEY,
                            nombre TEXT NOT NULL,
                            edad INTEGER CHECK (edad > 0), 
                            salario DOUBLE,
                            es_genio BOOLEAN,
                            f_inicio DATE
                        );
                    """
                ]

            # Ejecuta la sentencia de creación de la tabla
            for tabla in tablas:
                cursor.execute(tabla)  # Ejecuta la sentencia SQL para crear la tabla
                bd.commit()  # Confirma los cambios realizados en la base de datos

            print("6/20 Tablas creadas correctamente PRESIONA ENTER")
            input()  # Espera que el usuario presione Enter para continuar

            print("7/20 Commit para guardar las tablas PRESIONA ENTER")
            input()  # Espera que el usuario presione Enter para confirmar

            bd.commit()  # Guardamos los cambios realizados en la base de datos hasta este momento
            print("8/20 Guardado correctamente PRESIONA ENTER")
            input()  # Espera que el usuario presione Enter para continuar




            # Inserción de datos en la tabla
            print("\nINSERTAR")
            print("*************************************************")
            print("9/20 Insertar valores para las tablas PRESIONA ENTER")
            input()  # Espera que el usuario presione Enter para continuar

            # Selección de datos a insertar dependiendo de la opción elegida
            if opc == 1:
                # Sentencia SQL para insertar datos en la tabla
                datos = [
                    """
                    INSERT INTO SebastianExpositoRuiz 
                    (id, nombre, edad, salario, es_genio, f_inicio)
                    VALUES
                    ('1', 'Sebastián Ruiz', 25, 2500.50, TRUE, '2024-06-16'),
                    ('2', 'Ana López', 30, 3100.75, FALSE, '2023-12-10'),
                    ('3', 'Carlos Pérez', 22, 1800.00, TRUE, '2024-01-20');
                    """
                ]
            elif opc == 2:
                # Sentencia SQL para insertar datos en la tabla
                datos = [
                    """
                    INSERT INTO SebastianExpositoRuiz 
                    (id, nombre, edad, salario, es_genio, f_inicio)
                    VALUES
                    ('1', 'Sebastián Ruiz', 25, 2500.50, TRUE, '2024-06-16'),
                    ('2', 'Ana López', 30, 3100.75, FALSE, '2023-12-10'),
                    ('3', 'Carlos Pérez', 22, 1800.00, TRUE, '2024-01-20');
                    """
                ]
            elif opc == 3:
                # Sentencia SQL para insertar datos en la tabla con formato diferente (valor '1' y '0' para es_genio)
                datos = [
                    """
                    INSERT INTO SebastianExpositoRuiz 
                    (id, nombre, edad, salario, es_genio, f_inicio)
                    VALUES
                    ('1', 'Sebastián Ruiz', 25, 2500.50, 1, '2024-06-16'),
                    ('2', 'Ana López', 30, 3100.75, 0, '2023-12-10'),
                    ('3', 'Carlos Pérez', 22, 1800.00, 1, '2024-01-20');
                    """
                ]

            # Ejecución de las sentencias de inserción de datos
            for sentencia in datos:
                cursor.execute(sentencia)

            print("10/20 Datos guardados exitosamente PRESIONA ENTER")
            input()  # Espera que el usuario presione Enter para continuar

            print("11/20 Commit para guardar las tablas PRESIONA ENTER")
            input()  # Espera que el usuario presione Enter para confirmar

            bd.commit()  # Guardamos los cambios realizados en la base de datos
            print("12/20 Guardado correctamente PRESIONA ENTER")
            input()  # Espera que el usuario presione Enter para continuar




            # Leer datos de la base de datos
            print("\nMOSTRAR")
            print("*************************************************")
            print("13/20 Mostrar los datos PRESIONA ENTER")
            input()  # Espera que el usuario presione Enter para continuar

            # Consulta SQL para seleccionar todos los registros
            sentencia = "SELECT * FROM SebastianExpositoRuiz;"
            cursor.execute(sentencia)

            # Mostrar los datos en un formato tabular
            tablitas = cursor.fetchall()  # Obtener todos los registros de la consulta
            print("+{:-<15}+{:-<15}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))
            print("|{:^15}|{:^15}|{:^10}|{:^50}|{:^10}|".format("ID", "Nombre", "Edad", "Salario", "Es_genio",
                                                                "F_inicio"))
            print("+{:-<15}+{:-<15}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))

            # Recorrer los registros y mostrarlos
            for id, nombre, edad, salario, es_genio, f_inicio in tablitas:
                print("|{:^15}|{:^15}|{:^10}|{:^50}|{:^10}|".format(id, nombre, edad, salario, es_genio, f_inicio))

            print("+{:-<15}+{:-<15}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))

            print("\n14/20 Continuar PRESIONA ENTER")
            input()  # Espera que el usuario presione Enter para continuar




            # Eliminar registros de la base de datos
            print("\nELIMINAR")
            print("*************************************************")
            print("15/20 Eliminar datos PRESIONA ENTER")
            input()  # Espera que el usuario presione Enter para continuar

            # Lista de ids a eliminar (aunque no se usa en la sentencia SQL)
            ids_a_eliminar = [(3,), (4,)]  # Cada id debe ser una tupla

            # Sentencia SQL para eliminar registros
            sentencia = "DELETE FROM SebastianExpositoRuiz WHERE es_genio = '1';"

            # Ejecutar la sentencia de eliminación
            cursor.execute(sentencia)

            print("16/20 Datos eliminados exitosamente PRESIONA ENTER")
            input()  # Espera que el usuario presione Enter para continuar

            print("17/20 Guardar los cambios realizados PRESIONA ENTER")
            input()  # Espera que el usuario presione Enter para confirmar
            bd.commit()  # Guardamos los cambios realizados

            print("18/20 Datos guardados PRESIONA ENTER")
            input()  # Espera que el usuario presione Enter para continuar




            # Leer nuevamente los datos de la base de datos
            print("\nMOSTRAR")
            print("*************************************************")
            print("19/20 Mostrar los datos PRESIONA ENTER")
            input()  # Espera que el usuario presione Enter para continuar

            # Consulta SQL para seleccionar todos los registros
            sentencia = "SELECT * FROM SebastianExpositoRuiz;"
            cursor.execute(sentencia)

            # Mostrar los datos en un formato tabular
            tablitas = cursor.fetchall()  # Obtener todos los registros de la consulta
            print("+{:-<15}+{:-<15}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))
            print("|{:^15}|{:^15}|{:^10}|{:^50}|{:^10}|".format("ID", "Nombre", "Edad", "Salario", "Es_genio",
                                                                "F_inicio"))
            print("+{:-<15}+{:-<15}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))

            # Recorrer los registros y mostrarlos
            for id, nombre, edad, salario, es_genio, f_inicio in tablitas:
                print("|{:^15}|{:^15}|{:^10}|{:^50}|{:^10}|".format(id, nombre, edad, salario, es_genio, f_inicio))

            print("+{:-<15}+{:-<15}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))

            print("\n20/20 Continuar PRESIONA ENTER")
            input()  # Espera que el usuario presione Enter para continuar

        except sqlite3.OperationalError as error:
            # En caso de error, se captura la excepción y se muestra el mensaje
            print("Error al abrir:", error)
        except mariadb.OperationalError as error:
            # En caso de error, se captura la excepción y se muestra el mensaje
            print("Error al abrir:", error)
        except psycopg.OperationalError as error:
            # En caso de error, se captura la excepción y se muestra el mensaje
            print("Error al abrir:", error)
