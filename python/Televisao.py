class Televisao():
    def __init__(self, marca, modelo, preco, ano):
        print("A tv {} foi criada".format(self))
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.ano = ano


t1 = Televisao("LG", "I3031", 1900, 2018)
print(t1.marca)
print(t1.modelo)
print(t1.preco)
print(t1.ano)