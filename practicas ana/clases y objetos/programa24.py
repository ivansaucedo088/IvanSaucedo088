Clase  Coche :
    def  __init__ ( self , marca , modelo , año ):
        yo mismo . marca  =  marca
        yo mismo.modelo = modelo
        yo mismo.año = año  
        self . en_marcha  =  Falso

    def  arrancar ( yo mismo ):
        self.en_marcha = True
        print ( "El coche" , self.marca , self.modelo , " ha arrancado . " )

    def  detener ( self ):
        self . en_marcha  =  Falso
        print ( "El coche" , self . marca , self . modelo , "se ha detenido." )

    def  mostrar_info ( self ):
        print ( "Marca:" , self.marca , " Modelo :" , self.modelo , " Año:" , self.año , " En marcha :" , ' Sí' if self.en_marcha else " No" )    

clase  Dueño :
    def  __init__ ( self , nombre , teléfono ):
        yo mismo.nombre = nombre
        yo mismo . teléfono  =  teléfono
        yo mismo . carros  = []

    def  comprar_carros ( self , carro ):
        ser . coches . añadir ( carro )
        print ( self.nombre , " Teléfono : " , self.telefono , " ha comprado un " , carro.marca , carro.modelo )

    def  vender_carros ( self , carro ):
        si  carro  en  si mismo . carros :
            ser . coches . quitar ( carro )
            print ( self.nombre , " está vendiendo un " , carro.marca , carro.modelo )
        demás :
            print ( self.nombre , " no tiene un " , carro.marca , carro.modelo , " para vender " )

    def  alquilar_carros ( self , carro ):
        si  carro  en  si mismo . carros :
            print ( self.nombre , " está rentando un " , carro.marca , carro.modelo )
        demás :
            print ( self.nombre , " no tiene uno " , carro.marca , carro.modelo , " para alquilar " )

# Crear dos objetos a partir de la clase Coche
coche1  =  Coche ( "Toyota" , "Corolla" , 2020 )
coche2  =  Coche ( "Honda" , "Civic" , 2018 )

# Crear tres objetos a partir de la clase Dueño
carro1  =  Dueño ( "Carlos" , "61282625262" )
carro2  =  Dueño ( "Angel" , "61485423262" )
carro3  =  Dueño ( "Yamir" , "61527282636" )

#Usar algunos métodos y métodos
coche1 . mostrar_info ()
coche1 .arrancar ( )
coche1 . detener ()

coche2 . mostrar_info ()
coche2 .arrancar ( )
coche2 . detener ()

# Primero, los dueños deben comprar los coches antes de poder venderlos o alquilarlos.
carro2 . comprar_carros ( coche1 )
carro3 . comprar_carros ( coche2 )

# Ahora pueden vender o alquilar
carro2 . vender_carros ( coche1 )
carro3 . alquilar_carros ( coche2 )