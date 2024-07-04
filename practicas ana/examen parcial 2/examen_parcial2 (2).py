# clase principal o clase padre
class musica:
    # Atributos de la clase musica
    def __init__(self, nombre, genero, tipo):
        self.nombre = nombre
        self.genero = genero
        self.tipo = tipo
        self.popularidad = None

    # metodos de la clase musica
    def tocar(self):
        print(self.nombre, "está tocando música de género", self.genero)

    def pausar(self):
        print(self.nombre, "ha pausado la música")

    def reproducir(self):
        print("El tipo de música es", self.tipo)

    def mostrar_popularidad(self):
        print("La popularidad de la música es:", self.popularidad)

    # metodo traído de la clase premio (Dependencia)
    def premiar(self):
        print(self.nombre, "ha ganado un premio")


# clase de dependencia
class premio:
    # Atributos de la clase premio (Dependencia)
    def __init__(self, categoria, año):
        self.categoria = categoria
        self.año = año

    # metodos de la clase premio (Dependencia)
    def mostrar_categoria(self):
        print("El premio es en la categoría", self.categoria, "del año", self.año)


# clase de agregación
class oyente:
    # Atributos de la clase oyente (Agregación)
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    # metodos de la clase oyente (Agregación)
    def escuchar_musica(self):
        print(self.nombre, "está escuchando música")

    def recomendar(self):
        print(self.nombre, "está recomendando esta música")

    def opinar(self):
        print(self.nombre, "está opinando sobre la música")


# clase de herencia
class musico(oyente):
    def __init__(self, nombre, edad, genero, instrumento):
        super().__init__(nombre, edad, genero)
        self.instrumento = instrumento

    # metodos de la clase musico (Herencia)
    def tocar_instrumento(self):
        print(self.nombre, "está tocando el instrumento:", self.instrumento)

    def componer(self):
        print(self.nombre, "está componiendo una canción")

    # metodo heredado de la clase oyente
    def opinar(self):
        super().opinar()
        print(self.nombre, "está opinando como músico")


# clase de asociación
class conciertos:
    # Atributos de la clase conciertos (Asociación)
    def __init__(self, id, capacidad, estado):
        self.id = id
        self.capacidad = capacidad
        self.estado = estado

    # metodos de la clase conciertos (Asociación)
    def mostrar_estado(self):
        print("El concierto está en estado", self.estado)

    def mostrar_capacidad(self):
        print("El concierto tiene una capacidad de", self.capacidad, "asistentes")

    def mostrar_id(self):
        print("El concierto tiene el identificador", self.id)


# clase de composición
class canciones:
    # Atributos de la clase canciones (Composición)
    def __init__(self, estilo, duracion, popularidad):
        self.estilo = estilo
        self.duracion = duracion
        self.popularidad = popularidad

    # metodos de la clase canciones (Composición)
    def mostrar_estilo(self):
        print("El estilo de la canción es:", self.estilo)

    def mostrar_duracion(self):
        print("La duración de la canción es:", self.duracion)

    def mostrar_popularidad(self):
        print("La popularidad de la canción es:", self.popularidad)



# Objetos de la clase musica
musica1 = musica("concierto de Año Nuevo", "Clásica", "Instrumental")
musica2 = musica("Fiesta de Verano", "Pop", "Vocal")
musica3 = musica("Jazz en la Noche", "Jazz", "Instrumental")

# Objetos de la clase premio (Dependencia)
premio1 = premio("Mejor Álbum", 2021)
premio2 = premio("Mejor Canción", 2022)

# Objetos de la clase oyente (Agregación)
oyente1 = oyente("Carlos", 28, "Masculino")
oyente2 = oyente("Ana", 22, "Femenino")

# Objetos de la clase musico (Herencia)
musico1 = musico("Luis", 34, "Masculino", "Guitarra")
musico2 = musico("Laura", 27, "Femenino", "Piano")

# Objetos de la clase conciertos (Asociación)
concierto1 = conciertos(1, 500, "Agotado")
concierto2 = conciertos(2, 300, "Disponible")

# Objetos de la clase canciones (Composición)
cancion1 = canciones("Rock", "3:45", "Alta")
cancion2 = canciones("Pop", "4:10", "Media")
cancion3 = canciones("Jazz", "5:00", "Alta")

# Función del menú interactivo
def menu():
    while True:
        print("Escoge que informacion quieres ver:")
        print("1. Estado de los conciertos")
        print("2. Opinion de musicos sobre musica")
        print("3. Escuchar musica (oyente)")
        print("4. Ver premios")
        print("5. Salir")

        opcion = input("Selecciona una opciun: ")

        if opcion == '1':
            concierto1.mostrar_estado()
            concierto2.mostrar_estado()
        elif opcion == '2':
            musico1.opinar()
            musico2.opinar()
        elif opcion == '3':
            oyente1.escuchar_musica()
            oyente2.escuchar_musica()
        elif opcion == '4':
            premio1.mostrar_categoria()
            premio2.mostrar_categoria()
        elif opcion == '5':
            print("Saliendo del menu")
            break
        else:
            print("Opcion no valida, intenta de nuevo.")

# Ejecutar el menú interactivo
menu()
