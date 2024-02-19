#Clase fecha
class fecha:
    #Función constructora de los atributos
    def __init__(self, dd, mm, aa):
        self.dd = dd
        self.mm = mm
        self.aa = aa
    #Funciónes set
    def setDia(self, dia):
        self.dd = dia
    def setMes(self, mes):
        self.mm = mes
    def setA(self, year):
        self.aa = year
    #Funciónes get
    def getDia(self):
        return self.dd
    def getMes(self):
        return self.mm
    def getA(self):
        return self.aa
    #Función __str__ para definir que aparecerá en consola al hacer un print(fecha)
    def __str__(self):
        return f"{self.dd}/{self.mm}/{self.aa}"

#Clase dirección
class direccion:
   #Función constructora de los atributos 
    def __init__(self, calle, nomenclatura, barrio, ciudad, edificio, apto):
        self.calle = calle
        self.nomenclatura = nomenclatura
        self.barrio = barrio
        self.ciudad = ciudad
        self.edificio = edificio
        self.apto = apto
    #Funciónes set
    def setCalle(self, calle):
        self.calle = calle
    def setNomenclatura(self, nomenclatura):
        self.nomenclatura = nomenclatura
    def setBarrio(self, barrio):
        self.barrio = barrio
    def setCiudad(self, ciudad):
        self.ciudad = ciudad
    def setEdificio(self, edificio):
        self.edificio = edificio
    def setApto(self, apto):
        self.apto = apto
    #Funciónes get
    def getCalle(self):
        return self.calle
    def getNomenclatura(self):
        return self.nomenclatura
    def getBarrio(self):
        return self.barrio
    def getCiudad(self):
        return self.ciudad
    def getEdificio(self):
        return self.edificio
    def getApto(self):
        return self.apto
    #Función toString
    def toString(self):
        print("Calle:", self.calle,"Nomenclatura:", self.nomenclatura, "Barrio:", self.barrio, "Ciudad:", self.ciudad,
              "Edificio:", self.edificio, "Apto:", self.apto)
    #Función __str__, esta función hace basicamente lo mismo que toString, asi que la de arriba se vuelve redundante peeero pues la voy a dejar ahi
    def __str__(self):
        return f"Calle: {self.calle}, Nomenclatura: {self.nomenclatura}, Barrio: {self.barrio}, Ciudad: {self.ciudad}, Edificio: {self.edificio}, Apto: {self.apto}"

#Clase usuario, la principal del programa
class usuario:
    #función constructora de los atributos
    def __init__(self, nombre, id, dd, mm, aa, ciudad_nacimiento, tel, email, calle, nomenclatura, barrio, ciudad, edificio, apto):
        self.nombre = nombre
        self.id = id
        self.fecha_nacimiento = fecha(dd, mm, aa)
        self.ciudad_nacimiento = ciudad_nacimiento
        self.tel = tel
        self.email = email
        self.dir = direccion(calle, nomenclatura, barrio, ciudad, edificio, apto)
    #Funciones set
    def setNombre(self, nombre):
        self.nombre = nombre
    def setId(self, id):
        self.id = id
    def setFecha_Nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento
    def setCiudad_Nacimiento(self, ciudad_nacimiento):
        self.ciudad_nacimiento = ciudad_nacimiento
    def setTel(self, tel):
        self.tel = tel
    def setEmail(self, email):
        self.email = email
    def setDir(self, dir):
        self.dir = dir
    #Funciones Get
    def getNombre(self):
        return self.nombre
    def getId(self):
        return self.id
    def getFecha_Nacimiento(self):
        return self.fecha_nacimiento
    def getCiudad_Nacimiento(self):
        return self.ciudad_nacimiento
    def getTel(self):
        return self.tel
    def getEmail(self):
        return str(self.email)
    def getDir(self):
        return self.dir
    #Función toString, esto puede ser cambiado por un __str__(self) y haría lo mismo realmente. lo dejo para hacer el ejemplo
    def toString(self):
        print("Nombre:", self.nombre, "Id:", self.id, "Fecha de Nacimiento:", self.fecha_nacimiento, 
              "Ciudad de Nacimiento:", self.ciudad_nacimiento, "Telefono:", self.tel, "Email:", self.email, "Dirección:", self.dir)

#Programa principal 1, Crear objeto tipo fecha

Date = fecha(10, 7, 2004)
print(Date)

#Crear objeto tipo dirección

Direction = direccion(43, "55A", "Santa Maria", "Medellín", "47", "Null")
print(Direction)

#Crear objeto tipo usuario

Mi_Usuario = usuario("Juan Miguel", 1040, 10, 7, 2004, "Medellín", 3725482, "judurango@unal", 43, "55A", "Santa Marta", "Bogotá", "Null", "Null")
Mi_Usuario.toString()