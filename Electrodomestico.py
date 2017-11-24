class Electrodomestico(object):

    def __init__(self, precioBase, color, consumoEnergetico, peso):
        self.precioBase=precioBase
        self.color = color
        self.consumoEnergetico=consumoEnergetico   #entre A-F
        self.peso=peso
        global precioFinal

    def comprobarConsumoEnergetico(self,):
        if (consumoEnergetico =="A"):
            self.precioBase=100
        elif (consumoEnergetico =="B"):
            self.precioBase=80
        elif (consumoEnergetico =="C"):
            self.precioBase=60
        elif (consumoEnergetico =="D"):
            self.precioBase=50
        elif (consumoEnergetico =="E"):
            self.precioBase=30
        elif (consumoEnergetico =="F"):
            self.precioBase=10
        else:
            self.precioBase=0
        #variable para obtener el precio final
        self.precioFinal = self.precioBase

    def comprobarPeso(self):
        if (peso>0 and peso <= 19):
            self.precioFinal() + 10
        elif (peso>19 and peso <=49):
            self.precioFinal() + 50
        elif (peso>49 and peso <=79):
            self.precioFinal() + 80
        elif (peso > 80):
            self.precioFinal() + 100


    def precioFinal(self):
        #Especifica el consumo energetico
        self.comprobarConsumoEnergetico()
        #Comprueba el peso
        self.comprobarPeso()
        return self.precioFinal()
