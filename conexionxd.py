import mysql.connector
from mysql.connector import Error

# creamos la conexion
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='hospital',
            user='root',
            password=''
        )
        if connection.is_connected():
            # mensaje de estado
            print("conexion exitosa")
            return connection
    except Error as e:
        print(f"error al conectar {e}")
        return None

# nuestra clase paciente 
class Paciente:
    def __init__(self, id, nombre, apellido, edad, diagnostico):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.diagnostico = diagnostico

    def __str__(self):
        return f"id: {self.id}, nombre: {self.nombre} {self.apellido}, edad: {self.edad}, diagnostico: {self.diagnostico}"

# clase gestion de paceintes1
class GestorPaciente:
    def __init__(self):
        self.connection = create_connection()
        if self.connection is None:
            raise Exception("error al conectar")
        self.cursor = self.connection.cursor()
    
    def agregar_paciente(self, paciente):
        try:
            query = "INSERT INTO paciente (nombre, apellido, edad, diagnostico) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (paciente.nombre, paciente.apellido, paciente.edad, paciente.diagnostico))
            self.connection.commit()
            print("paciente agregado")
        except Error as e:
            print(f"error al agregar paciente: {e}")

    def actualizar_paciente(self, paciente):
        try:
            query = "UPDATE paciente SET nombre = %s, apellido = %s, edad = %s, diagnostico = %s WHERE id = %s"
            self.cursor.execute(query, (paciente.nombre, paciente.apellido, paciente.edad, paciente.diagnostico, paciente.id))
            self.connection.commit()
            print("paciente actualizado")
        except Error as e:
            print(f"error al actualizar: {e}")

    def eliminar_paciente(self, paciente_id):
        try:
            query = "DELETE FROM paciente WHERE id = %s"
            self.cursor.execute(query, (paciente_id,))
            self.connection.commit()
            print("paciente eliminado")
        except Error as e:
            print(f"error al eliminar: {e}")

    def consultar_paciente(self, paciente_id):
        try:
            query = "SELECT * FROM paciente WHERE id = %s"
            self.cursor.execute(query, (paciente_id,))
            result = self.cursor.fetchone()
            if result:
                return Paciente(*result)
            else:
                print("paciente no encontrado")
                return None
        except Error as e:
            print(f"error al consultar: {e}")

    def listar_pacientes(self):
        try:
            query = "SELECT * FROM paciente"
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return [Paciente(*row) for row in results]
        except Error as e:
            print(f"error al listar: {e}")

def menu():
    try:
        gestor = GestorPaciente()
    
        while True:
            print("\nmenu de gestion de pacientes")
            print("1. agregar paciente")
            print("2. actualizar paciente")
            print("3. eliminar paciente")
            print("4. consultar paciente ")
            print("5. listar pacientes")
            print("6. salir")
            
            opcion = input("selecciona una opcion: ")
            
            if opcion == '1':
                nombre = input("nombre: ")
                apellido = input("apellido: ")
                edad = int(input("edad: "))
                diagnostico = input("diagnostico: ")
                paciente = Paciente(None, nombre, apellido, edad, diagnostico)
                gestor.agregar_paciente(paciente)
            
            elif opcion == '2':
                paciente_id = int(input("id del paciente: "))
                paciente = gestor.consultar_paciente(paciente_id)
                if paciente:
                    nombre = input(f"nuevo nombre ({paciente.nombre}): ")
                    apellido = input(f"nuevo apellido ({paciente.apellido}): ")
                    edad = int(input(f"nueva edad ({paciente.edad}): "))
                    diagnostico = input(f"nuevo diagnostico ({paciente.diagnostico}): ")
                    paciente.nombre = nombre if nombre else paciente.nombre
                    paciente.apellido = apellido if apellido else paciente.apellido
                    paciente.edad = edad if edad else paciente.edad
                    paciente.diagnostico = diagnostico if diagnostico else paciente.diagnostico
                    gestor.actualizar_paciente(paciente)
            
            elif opcion == '3':
                paciente_id = int(input("Iid del paciente a eliminar: "))
                gestor.eliminar_paciente(paciente_id)
            
            elif opcion == '4':
                paciente_id = int(input("id del paciente a consultar: "))
                paciente = gestor.consultar_paciente(paciente_id)
                if paciente:
                    print(paciente)
            
            elif opcion == '5':
                pacientes = gestor.listar_pacientes()
                for paciente in pacientes:
                    print(paciente)
            
            elif opcion == '6':
                print("saliendo...")
                break
            
            else:
                print("opcion no valida, intenta de nuevo")
            
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    menu()
