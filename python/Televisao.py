class Televisao():
    def __init__(self, marca, n_canais, preco, ano):
        print("A tv {} foi criada".format(self))
        self.marca = marca
        self.n_canais = n_canais
        self.preco = preco
        self.ano = ano
        self._ligada = False
        
    def aumenta_canal(self):
        self.n_canais += 1
        
    def diminui_canal(self):
        self.n_canais -= 1
        
    def liga_tv(self):
        self._ligada = True
        
t1 = Televisao("LG", 40, 1900, 2018)
t1.aumenta_canal()
print(t1.n_canais)

for i in range(6):
    t1.diminui_canal()
    
print(t1.n_canais)

print(t1)

tv_nova = t1
print(tv_nova)

tv_nova = None
print(tv_nova)

## Encapsulamento a partir daqui

## Atributos privados

print(t1.ligada)
t1.liga_tv()
print(t1.ligada)