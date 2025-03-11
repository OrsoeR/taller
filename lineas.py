import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="OrsoeR22",
            database="dbtaller"
        )
        return conexion
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None

def ejecutar_crud(conexion, tabla):
    while True:
        print(f"\nGestionando {tabla}")
        print("A. Ver registros")
        print("B. Insertar registro")
        print("C. Actualizar registro")
        print("D. Eliminar registro")
        print("E. Volver al menú principal")
        opcion = input("Seleccione una opción: ").upper()
        cursor = conexion.cursor()

        if opcion == "A":
            cursor.execute(f"SELECT * FROM {tabla}")
            for registro in cursor.fetchall():
                print(registro)
        elif opcion == "B":
            valores = input("Ingrese los valores separados por coma: ")
            datos = tuple(valores.split(","))
            sql = f"INSERT INTO {tabla} VALUES ({', '.join(['%s'] * len(datos))})"
            cursor.execute(sql, datos)
            conexion.commit()
        elif opcion == "C":
            id_registro = input("Ingrese el ID del registro a actualizar: ")
            columna = input("Ingrese la columna a modificar: ")
            nuevo_valor = input("Ingrese el nuevo valor: ")
            sql = f"UPDATE {tabla} SET {columna} = %s WHERE id = %s"
            cursor.execute(sql, (nuevo_valor, id_registro))
            conexion.commit()
        elif opcion == "D":
            id_registro = input("Ingrese el ID del registro a eliminar: ")
            cursor.execute(f"DELETE FROM {tabla} WHERE id = %s", (id_registro,))
            conexion.commit()
        elif opcion == "E":
            break
        cursor.close()

def main():
    conexion = conectar()
    if not conexion:
        return

    while True:
        print("\nMenú Principal")
        print("1. Líneas de Investigación")
        print("2. Tipos de Proyecto")
        print("3. Profesores")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_crud(conexion, "lineainv")
        elif opcion == "2":
            ejecutar_crud(conexion, "tipoproyecto")
        elif opcion == "3":
            ejecutar_crud(conexion, "profesor")
        elif opcion == "4":
            break
    conexion.close()

if __name__ == "__main__":
    main()
