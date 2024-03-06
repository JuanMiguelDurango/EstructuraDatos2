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
    #Función __str__, esto puede ser cambiado por un toString y haría lo mismo realmente. Pero este es más conveniente >:3
    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id}, Fecha de Nacimiento: {self.fecha_nacimiento}, Ciudad de Nacimiento: {self.ciudad_nacimiento}, Telefono: {self.tel}, Email: {self.email}, Direccion: {self.dir}"

usuario0 = usuario("Jose Juan", 0, 10, 7, 2041, "Medellin", 3715382, "Judsq@unal", 47, "55A", "Santa", "cali", "", "")
usuario1 = usuario("Miguel", 1, 15, 2, 2001, "Bogota", 3715, "jmiguld@unal", 12, "65B", "lasti", "Lima", "", "")
usuario2 = usuario("Nicolas", 2, 31, 12, 2004, "Fondo de bikini", 612736, "Nilobj@unal", 43, "76K", "Crustaceo", "Cascarudo", "", "")
usuario3 = usuario("Mary", 3, 21, 8, 2007, "Bajoterra", 716387,"Mar1@unal", 75, "57C", "Babosa", "Fria", "", "" )
usuario4 = usuario("Paquito Alimañana", 4, 30, 2, 1914, "Stalingrado", 1983981, "alemaniacool@comunismo.com", 42, "98JK", "springfield", "cualquiera", "trece", 14)

class agenda:
    def __init__(self):
        self.capacity = 5
        self.registro = [None] * self.capacity
        self.no_reg = 0

    def agregar(self, U:usuario):
        if self.buscar(U.id) == -1:
            return False
        if self.no_reg < self.capacity:
            self.registro[self.no_reg] = U
            self.no_reg += 1
            return True
        else:
            return False 

    
    def buscar(self, id):
        for i in range(len(self.registro)):
            if self.registro[i] == None:
                return i
            elif self.registro[i].id == id:
                return i
        return -1
    
    def eliminar(self, id):
        k = self.buscar(id)
        if k == -1:
            return False
        else:
            self.registro.pop(k)
            self.registro.append(None)
            self.no_reg -= 1
            return True
    
    def toFile(self):
        with open('agenda2.txt', 'w') as f:
            for usuario in self.registro:
                if usuario is not None:
                    f.write(str(usuario) + "\n")
    
    def importar(self):
        with open('agenda.txt', 'r') as f:
            for line in f:
                data = line.split(',')
                nombre = data[0]
                id = int(data[1])
                dd, mm, aa = map(int, data[2].split('/'))
                ciudad_nacimiento = data[3]
                tel = int(data[4])
                email = data[5]
                calle = int(data[6])
                nomenclatura = data[7]
                barrio = data[8]
                ciudad = data[9]
                edificio = data[10]
                apto = data[11].strip()

                nuevo_usuario = usuario(nombre, id, dd, mm, aa, ciudad_nacimiento, tel, email, calle, nomenclatura, barrio, ciudad, edificio, apto)
                self.agregar(nuevo_usuario)

array = agenda()
array.importar()
for user in array.registro:
    if user is not None:
        print(user)
array.eliminar(0)
array.toFile()