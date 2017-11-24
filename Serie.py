class Serie(object):

    def __init__(self, titulo, numTemporadas, entregado, genero, valor):
        self.titulo=titulo
        self.numTemporadas= numTemporadas
        self.entregado=entregado
        self.genero = genero
        self.valor = valor

    #true= serie entregada
    def entregar(self):
        self.entregado=true
