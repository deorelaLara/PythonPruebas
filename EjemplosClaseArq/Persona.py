"""
CLASE PERSONA
    -5 ATRIBUTOS
        2 DE LOS ATRIBUTOS TIENEN QUE SER PESO Y ESTATURA
    -FUNCION QUE OBTENGA EL INDICE DE MASA CORPORAL
"""
class Persona(object):
    #CONSTRUCTOR
    def __init__(self, nombre, edad, peso, estatura, pasatiempo):

        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.estatura = estatura
        self.pasatiempo = pasatiempo

    #Get & Set
    def set_nombre(self, nombre):
        self.nombre=nombre
    def get_nombre(self):
        return self.nombre
    def set_edad(self, edad):
        self.edad = edad
    def get_edad(self):
        return self.edad
    def set_peso(self, peso):
        self.edad = peso
    def get_peso(self):
        return self.peso
    def set_estatura(self, estatura):
        self.estatura = estatura
    def get_estatura(self):
        return self.estatura
    def set_pasatiempo(self, pasatiempo):
        self.pasatiempo = pasatiempo
    def get_pasatiempo(self):
        return self.pasatiempo
    #FUNCION INDICE DE MASA CORPORAL
    def indiceM(self, peso, altura):
        return peso / altura **2
    #STRING
    def __str__(self):
        return f'Nombre: {self.nombre}\nEdad: {self.edad} años\nPeso:{self.peso} kg\nEstatura:{self.estatura}cm\nPasatiempo:{self.pasatiempo}'

#OBJETO
persona = Persona('Herqlño', '21','50 kg','1.65', 'Herqlñear')
print(persona)
print(persona.indiceM(peso=60, altura=1.75))