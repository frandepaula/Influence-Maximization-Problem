
class Vertice:
    #Cada vertice tem um vetor para saber quem são seus vizinhos e seu status
    def __init__(self, qtdVertices):
        self.qtdVertices = qtdVertices
        self.vizinhos = []
        self.status = "inativo"