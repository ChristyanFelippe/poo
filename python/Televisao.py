class Televisao():
    def __init__(self, marca, n_canais, preco, ano):
        print("A tv {} foi criada".format(self))
        self.marca = marca
        self.n_canais = n_canais
        self.preco = preco
        self.ano = ano
        
    def aumenta_canal(self):
        self.n_canais += 1
        
    def diminui_canal(self):
        self.n_canais -= 1


t1 = Televisao("LG", 40, 1900, 2018)
print(t1.marca)
print(t1.n_canais)
print(t1.preco)
print(t1.ano)

t1.aumenta_canal()
print(t1.n_canais)