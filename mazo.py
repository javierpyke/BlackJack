import random as R

class Carta(object):

    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def get_palo(self):
        return self.palo

    def set_palo(self, palo):
        self.palo = palo

    def get_numero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero


class Carta_poker(Carta):

    def __init__(self, numero, palo):
        super().__init__(numero, palo)

    def __str__(self):
        palos = [" ", "♦", "♣", "♠", "♥"]
        numeros = ["", "A", "2", "3", "4", "5",
                   "6", "7", "8", "9", "10", "J", "Q", "K"]
        return "[" + numeros[self.get_numero()] + palos[self.get_palo()] + "]"

#                           [2,2][3,1][2,3]..........[1,2]


class Mazo(object):

    def __init__(self):
        self.las_cartas = []

    def sacar(self):
        return self.las_cartas.pop(0)

    def poner(self, carta):
        self.las_cartas.append(carta)

    def mezclar(self):
        R.shuffle(self.las_cartas)
    
    def __str__(self):
        cadena = ""
        for c in self.las_cartas:
            cadena += str(c)
        return cadena
        

    def llenar(self):
        pass

    def hayCartas(self):
        return len(self.las_cartas) > 0

class Mazo_poker(Mazo):
    
    def __init__(self):
        super().__init__()
        self.llenar()
    
    def llenar(self):
        for n in range(1,14):
            for p in range(1,5):
                self.las_cartas.append(Carta_poker(n,p))


class Mazo_blackjack(Mazo):
    def __init__(self):
        super().__init__()
        

    def llenar(self):
        for m in range(1,11):#RANGO 1..10
            for n in range(1,14):
                for p in range(1,5):
                    self.las_cartas.append(Carta_poker(n,p))
    
    
def main():
    # c = Carta_poker(3, 4)

    # print(c)

    # m = Mazo_poker()
    # m.llenar()
    
    # print(str(m))

    mbj = Mazo_blackjack()
    mbj.llenar()
    print(str(mbj))

if __name__ == "__main__":
    main()
