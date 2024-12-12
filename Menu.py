# import mysql.connector
import sqlite3
import mariadb
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
            print("2- MySQL")
            print("3- SQLite3")
            print("0- Salir")
            print("*************************")

            #Pedir opcion de las bases de datos disponibles
            opc = int(input("\nIntroduzca alguna opcion: "))

            # Comprobar que no sea nulo
            if not opc:
                print("No escribiste nada")
                exit()

            if opc == 1:
                print("\nBienvenido a PostgreSQL!")
                self.crudPostgreSQL()
            elif opc == 2:
                print("\nBienvenido a MariaDB!")
                self.crudMariaDB()
            elif opc == 3:
                print("\nBienvenido a SQLite3!")
                self.crudSQLite3()
            elif opc == 0:
                print("Saliendo del programa")
                self.ejecutar = False
                exit()




    def crudPostgreSQL(self):
        pass

    def crudMariaDB(self):
        #Conectar a la base de datos ademas del cursor
        print("\n*************************************************")
        print("Conectar con la base de datos PRESIONA ENTER")
        input()

        # Conectar con MariaDB
        try:
            db = mariadb.connect(
                user="root",
                password="",
                host="localhost",
                port=3306,
                database="dbpython"

            )
            print("Te has conecetado con exito")
        except mariadb.Error as e:
            print(f"Error de conexion con la db MariaDB: {e}")

        print("\nHabilitar el cursor PRESIONA ENTER")
        input()
        cur = db.cursor()
        print("Cursor habilitado con exito PRESIONA ENTER")
        input()

        self.maldades(db, cur)


    def crudSQLite3(self):

        #Conectar a la base de datos ademas del cursor
        print("\n*************************************************")
        print("Conectar con la base de datos PRESIONA ENTER")
        input()

        bd = sqlite3.connect("SebastianExpositoRuiz.db")
        print("Base de datos abierta")

        print("\nHabilitar el cursor PRESIONA ENTER")
        input()
        cursor = bd.cursor()
        print("Cursor habilitado con exito PRESIONA ENTER")
        input()

        self.maldades(bd, cursor)



    def maldades(self, bd, cursor):
        # CRUD
        try:
            print("\n*************************************************")
            print("CRUD")
            print("*************************************************")

            print("\nCREAR")
            print("*************************************************")
            print("Crear tablas PRESIONA ENTER")
            input()


            cursor.execute("DROP TABLE IF EXISTS SebastianExpositoRuiz")
            bd.commit()


            # Crear datos
            tablas = [
                """
                    CREATE TABLE IF NOT EXISTS SebastianExpositoRuiz(
                        autor TEXT NOT NULL,
                        genero TEXT NOT NULL,
                        precio REAL NOT NULL,
                        titulo REAL NOT NULL,
                        coso REAL NOT NULL
                    );
                """
            ]
            for tabla in tablas:
                cursor.execute(tabla)

            print("Tablas creadas correctamente PRESIONA ENTER")
            input()

            print("\nCommit para guardar las tablas PRESIONA ENTER")
            input()
            bd.commit()  # Guardamos los cambios al terminar el ciclo
            print("Guardado correctamente PRESIONA ENTER")
            input()

            # Insertar datos
            print("\nINSERTAR")
            print("*************************************************")
            print("Insertar valores para las tablas PRESIONA ENTER")
            input()

            libros = [
                """
                INSERT INTO SebastianExpositoRuiz
                (autor, genero, precio, titulo, coso)
                VALUES
                ('Stephen King', 'Terror', 115,'Cementerio de animales', '1'),
                ('Alfred Bester', 'Ciencia ficción', 200,'Las estrellas, mi destino', '2'),
                ('Margaret Atwood1', 'Ciencia ficción', 150,'El cuento de la cfriada', '3'),
                ('Margaret Atwood2', 'Ciencia ficción', 150,'El cuento de la crriada', '4'),
                ('Margaret Atwood3', 'Ciencia ficcióna', 1530,'El cuento de la criadae', '5');
                """
            ]
            for sentencia in libros:
                cursor.execute(sentencia)

            print("Datos guardados exitosamente PRESIONA ENTER")
            input()

            print("\nCommit para guardar las tablas PRESIONA ENTER")
            input()

            bd.commit()  # Guardamos los cambios al terminar el ciclo
            print("Guardado correctamente PRESIONA ENTER")
            input()

            # Leer datos
            print("\nMOSTRAR")
            print("*************************************************")
            print("Mostrar los datos PRESIONA ENTER")
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

            print("\nContinuar PRESIONA ENTER")
            input()

            # Eliminar
            print("\nELIMINAR")
            print("*************************************************")
            print("Eliminar datos PRESIONA ENTER")
            input()

            # Lista de rowid a eliminar
            ids_a_eliminar = [(3,), (4,)]  # Cada id debe ser una tupla

            # Sentencia para eliminar
            sentencia = "DELETE FROM SebastianExpositoRuiz WHERE coso = ?;"

            # Eliminar los registros con executemany
            cursor.executemany(sentencia, ids_a_eliminar)

            print("\nDatos eliminados exitosamente PRESIONA ENTER")
            input()

            print("Guardar los cambios realizados PRESIONA ENTER")
            input()
            bd.commit()

            print("\nDatos guardados PRESIONA ENTER")
            input()

            # Leer datos
            print("\nMOSTRAR")
            print("*************************************************")
            print("Mostrar los datos PRESIONA ENTER")
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

            print("\nContinuar PRESIONA ENTER")
            input()

        except sqlite3.OperationalError as error:
            print("Error al abrir:", error)



