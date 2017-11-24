
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Main.py
#
#  Copyright 2016 manrique <https:/github.com/luisFcoOrtiz>
#
class Persona():

    def __init__(self, nombre, edad, dni, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def calcularIMC(self):
        global imc
        imc=self.peso/self.altura**2
        if(imc<24.9 and imc>=18):
            return 0
        elif(imc>=25):
            return 1
        elif(imc<18):
            return -1

    def esMayorDeEdad(self):
        if (self.edad>=18):
            return true
        elif(self.edad<18):
            return false

    def getIMC(self):
        return imc

    def introducirSexo(self,  sexo):
        self.sexo=sexo

    def toString(self):
        print("Datos personales: "+self.nombre+" | edad:"+str(self.edad)+" | dni:"+self.dni+" | sexo:"+self.sexo)
