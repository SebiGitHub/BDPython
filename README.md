## Qué es
Proyecto en Python orientado a practicar acceso a bases de datos y operaciones CRUD, comparando distintos motores (MariaDB, SQLite y PostgreSQL) tiene funciones o módulos para conectarse a una base de datos, realizar consultas, insertar, actualizar o borrar datos — y otras operaciones de gestión de datos.

## Para qué sirve
BDPython sirve como backend simple y herramienta auxiliar para manejar datos desde Python. Puede ser útil para automatizar tareas, procesar datos en batch, realizar informes o servir como capa de datos en aplicaciones más complejas. También puede emplearse para prototipos rápidos donde Python es el lenguaje principal.

## Stack
- Python
- MariaDB / SQLite / PostgreSQL
- (Cliente) DBeaver y XAMP
- Librerías: `psycopg2`, `psycopg_binary`, `mariadb  ` y `sqlite3`

## Features
- Operaciones CRUD desde consola
- Conexión a distintos motores de base de datos
- Comparativa práctica entre motores (facilidad, configuración, uso, velocidad, estilo y respuesta)
- Manejo básico de errores y validaciones

## Capturas/GIF
<img width="563" height="660" alt="image" src="https://github.com/user-attachments/assets/fe22147d-06e9-42a8-97c9-0eac8a9f66a9" />
<img width="544" height="773" alt="image" src="https://github.com/user-attachments/assets/447cf53b-b5ff-4d25-89b8-11d57cb8a8c3" />
<img width="1083" height="721" alt="image" src="https://github.com/user-attachments/assets/1c2febdb-88b9-4b54-b8be-baee67a91c0a" />
<img width="1086" height="754" alt="image" src="https://github.com/user-attachments/assets/a87c460e-b540-4654-a53e-e9a486b5e5d6" />

## Cómo ejecutar
1. Clona el repo
2. (Opcional) Crea entorno virtual e instala dependencias:
   ```bash
   pip install -r requirements.txt
3. Configura credenciales (recomendado con variables de entorno): DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME [TODO]
4. Ejecuta: python main.py

## Qué aprendí
- Diferencias prácticas entre motores SQL al conectar desde Python
- Diseño de CRUD reusable (funciones/módulos)
- Buenas prácticas: separar config, evitar credenciales en código, manejo de errores
