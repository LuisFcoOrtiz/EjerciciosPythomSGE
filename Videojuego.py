class Videojuego():

    def __init__(self, titulo, horasEstimadas, entregado, genero, company):
        self.titulo=titulo
        self.horasEstimadas=horasEstimadas
        self.entregado=entregado
        self.genero=genero
        self.company=company

    def entregar(self):
        self.entregado=true
