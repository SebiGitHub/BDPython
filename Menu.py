# import mysql.connector
import sqlite3
import mariadb
import psycopg
import psycopg_binary
import sys


class Menu:
    def __init__(self):
        self.conn = None
        self.ejecutar = True



    def menu(self):
        while self.ejecutar == True:
            print("\nMENU DE BASES DE DATOS")
            print("*************************")
            print("1- PostgreSQL")
            print("2- MariaDB")
            print("3- SQLite3")
            print("0- Salir")
            print("*************************")

            #Pedir opcion de las bases de datos disponibles
            opc = input("\nIntroduzca alguna opcion: ")

            # Comprobar que no sea nulo
            if opc in ["0","1","2","3"]:
                if opc == "1":
                    print("\nBienvenido a PostgreSQL!")
                    self.crudPostgreSQL()
                elif opc == "2":
                    print("\nBienvenido a MariaDB!")
                    self.crudMariaDB()
                elif opc == "3":
                    print("\nBienvenido a SQLite3!")
                    self.crudSQLite3()
                elif opc == "0":
                    print("Saliendo del programa")
                    self.ejecutar = False
                    exit()
            else:
                print("Ingrese una opcion válida")





    def crudPostgreSQL(self):
        # Conectar a la base de datos ademas del cursor
        print("\n*************************************************")
        print("1/20 Conectar con la base de datos PRESIONA ENTER")
        input()

        # Conectar con MariaDB
        try:
            db = psycopg.connect(
                user="postgres",
                password="1234",
                host="localhost",
                port=5432,
                dbname="bdpython"

            )
            print("2/20 Te has conecetado con exito PRESIONA ENTER")
            input()

        except psycopg.Error as e:
            print(f"Error de conexion con la db MariaDB: {e}")

        print("3/20 Habilitar el cursor PRESIONA ENTER")
        input()
        cur = db.cursor()
        print("4/20 Cursor habilitado con exito PRESIONA ENTER")
        input()

        self.crud(db, cur)




    def crudMariaDB(self):
        #Conectar a la base de datos ademas del cursor
        print("\n*************************************************")
        print("1/20 Conectar con la base de datos PRESIONA ENTER")
        input()

        # Conectar con MariaDB
        try:
            db = mariadb.connect(
                user="root",
                password="",
                host="localhost",
                port=3306,
                database="bdpython"

            )
            print("2/20 Te has conectado con exito PRESIONA ENTER")
            input()

        except mariadb.Error as e:
            print(f"Error de conexion con la db MariaDB: {e}")

        print("3/20 Habilitar el cursor PRESIONA ENTER")
        input()
        cur = db.cursor()
        print("4/20 Cursor habilitado con exito PRESIONA ENTER")
        input()

        self.crud(db, cur)


    def crudSQLite3(self):

        #Conectar a la base de datos ademas del cursor
        print("\n*************************************************")
        print("1/20 Conectar con la base de datos PRESIONA ENTER")
        input()

        bd = sqlite3.connect("SebastianExpositoRuiz.db")
        print("2/20 Te has conectado con exito PRESIONA ENTER")
        input()

        print("3/20 Habilitar el cursor PRESIONA ENTER")
        input()
        cursor = bd.cursor()
        print("4/20 Cursor habilitado con exito PRESIONA ENTER")
        input()

        self.crud(bd, cursor)



    def crud(self, bd, cursor):
        # CRUD
        try:
            print("\n************")
            print("    CRUD")
            print("************")

            print("\nCREAR")
            print("*************************************************")
            print("5/20 Crear tablas PRESIONA ENTER")
            input()


            #Eliminar la tabla con mi nombre si es que existe para evitar posibles errores futuros.
            cursor.execute("DROP TABLE IF EXISTS SebastianExpositoRuiz")
            bd.commit()


            # Crear datos
            tablas = [
                """
                    CREATE TABLE IF NOT EXISTS SebastianExpositoRuiz(
                        autor TEXT NOT NULL,
                        genero TEXT NOT NULL,
                        precio REAL NOT NULL,
                        titulo TEXT NOT NULL,
                        coso REAL NOT NULL
                    );
                """
            ]
            for tabla in tablas:
                cursor.execute(tabla)

            print("6/20 Tablas creadas correctamente PRESIONA ENTER")
            input()

            print("7/20 Commit para guardar las tablas PRESIONA ENTER")
            input()
            bd.commit()  # Guardamos los cambios al terminar el ciclo
            print("8/20 Guardado correctamente PRESIONA ENTER")
            input()

            # Insertar datos
            print("\nINSERTAR")
            print("*************************************************")
            print("9/20 Insertar valores para las tablas PRESIONA ENTER")
            input()

            libros = [
                """
                INSERT INTO SebastianExpositoRuiz
                (autor, genero, precio, titulo, coso)
                VALUES
                ('Stephen King', 'Terror', 115, 'Cementerio de animales', '1'),
                ('Alfred Bester', 'Ciencia ficción', 200,'Las estrellas, mi destino', '2'),
                ('Margaret Atwood1', 'Ciencia ficción', 150,'El cuento de la cfriada', '3'),
                ('Margaret Atwood2', 'Ciencia ficción', 150,'El cuento de la crriada', '4'),
                ('Margaret Atwood3', 'Ciencia ficcióna', 1530,'El cuento de la criadae', '5');
                """
            ]
            for sentencia in libros:
                cursor.execute(sentencia)

            print("10/20 Datos guardados exitosamente PRESIONA ENTER")
            input()

            print("11/20 Commit para guardar las tablas PRESIONA ENTER")
            input()

            bd.commit()  # Guardamos los cambios al terminar el ciclo
            print("12/20 Guardado correctamente PRESIONA ENTER")
            input()

            # Leer datos
            print("\nMOSTRAR")
            print("*************************************************")
            print("13/20 Mostrar los datos PRESIONA ENTER")
            input()

            # Consulta SQL
            sentencia = "SELECT * FROM SebastianExpositoRuiz;"
            cursor.execute(sentencia)

            # Estructura del como se muestran los datos
            libros = cursor.fetchall()
            print("+{:-<15}+{:-<15}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))
            print("|{:^15}|{:^15}|{:^10}|{:^50}|{:^10}|".format("Autor", "Género", "Precio", "Título", "Coso"))
            print("+{:-<15}+{:-<15}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))

            for autor, genero, precio, titulo, coso in libros:
                print("|{:^15}|{:^15}|{:^10}|{:^50}|{:^10}|".format(autor, genero, precio, titulo, coso))

            print("+{:-<15}+{:-<15}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))

            print("\n14/20 Continuar PRESIONA ENTER")
            input()

            # Eliminar
            print("\nELIMINAR")
            print("*************************************************")
            print("15/20 Eliminar datos PRESIONA ENTER")
            input()

            # Lista de rowid a eliminar
            ids_a_eliminar = [(3,), (4,)]  # Cada id debe ser una tupla

            # Sentencia para eliminar
            sentencia = "DELETE FROM SebastianExpositoRuiz WHERE coso = '1';"

            # Eliminar los registros con executemany
            cursor.execute(sentencia)

            print("16/20 Datos eliminados exitosamente PRESIONA ENTER")
            input()

            print("17/20 Guardar los cambios realizados PRESIONA ENTER")
            input()
            bd.commit()

            print("18/20 Datos guardados PRESIONA ENTER")
            input()

            # Leer datos
            print("\nMOSTRAR")
            print("*************************************************")
            print("19/20 Mostrar los datos PRESIONA ENTER")
            input()

            # Consulta SQL
            sentencia = "SELECT * FROM SebastianExpositoRuiz;"
            cursor.execute(sentencia)

            # Estructura del como se muestran los datos
            libros = cursor.fetchall()
            print("+{:-<15}+{:-<15}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))
            print("|{:^15}|{:^15}|{:^10}|{:^50}|{:^10}|".format("Autor", "Género", "Precio", "Título", "Coso"))
            print("+{:-<15}+{:-<15}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))

            for autor, genero, precio, titulo, coso in libros:
                print("|{:^15}|{:^15}|{:^10}|{:^50}|{:^10}|".format(autor, genero, precio, titulo, coso))

            print("+{:-<15}+{:-<15}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))

            print("\n20/20 Continuar PRESIONA ENTER")
            input()

        except sqlite3.OperationalError as error:
            print("Error al abrir:", error)



