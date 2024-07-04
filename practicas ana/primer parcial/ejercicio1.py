class cancion:
    def __init__(self, nombre, duracion, artista, genero):
        self.nombre = nombre
        self.duracion = duracion
        self.artista = artista
        self.genero = genero

    def __str__(self):
        return f"{self.nombre} de {self.artista} duracion: {self.duracion} genero: {self.genero}" 

class album:
    def __init__(self, titulo, artista, año):
        self.titulo = titulo
        self.artista = artista
        self.año = año
        
    def añadir_cacion(self, cancion):
        if isinstance(cancion):
            self.cancion.append(cancion)
        
    def __str__(self):
        return f"album: {self.titulo} por {self.artista} del {self.año}"
    

class genero:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre
    
