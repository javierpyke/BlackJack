from mazo import Mazo_blackjack, Carta_poker
from random import randint


class Jugador(object):
    
    def __init__(self,nombre):
        self.nombre = nombre
        self.mano = Mazo_blackjack()
    
    def get_nombre(self):
        return self.nombre

    def set_nombre(self,nombre):
        self.nombre = nombre
    
    def __str__(self):
        return self.nombre + str(self.mano)
    
    def sumar_cartas(self):
        cartas = self.mano.las_cartas
        suma = 0
        cont_unos = 0
        for c in cartas:
            if c.get_numero() == 1:
                cont_unos += 1
            else:
                if c.get_numero() > 10:
                    suma += 10
                else:
                    suma += c.get_numero()       
        while suma + 11 < 21 and cont_unos > 0:
            suma += 11
            cont_unos -= 1 
        return suma + cont_unos
    
    def me_planto(self):
        pass

class jugador_cliente(Jugador):
    
    def __init__(self, nombre,fichas=100):
        super().__init__(nombre)
        self.fichas = fichas
    
    def get_fichas(self):
        return self.fichas
    
    def set_fichas(self,fichas):
        self.fichas=fichas
    
    def tiene_fichas(self):
        return self.fichas == 0
    
    def sumar_fichas(self,fichas):
        self.fichas += fichas
    
    def restar_fichas(self,fichas):
        self.fichas-=fichas
    
    
    def apuesto(self):
        pass    
    
    def me_planto(self):
        pass

class Jugador_Humano(jugador_cliente):
    
    def __init__(self, nombre ,fichas=100):
        super().__init__(nombre, fichas)
    
    def sePlanta(self):
        
        suma =  self.sumar_cartas() 
        if suma > 21:
            print(self.nombre,"  ",str(self.mano) , " ",suma," SE PASO!!!")    
            return True
        print("------------------")
        print(self.nombre,"  ",str(self.mano) , " ",suma)
        respuesta = input("SE PLANTA ? (S/N)").upper()
        if respuesta == 'S':
            print(self.nombre,"SE PLANTO CON ", suma)
            print("--------------------------------")
            return True
        return False

    def apuesta(self):
        suApuesta = int(input("HAGA SU APUESTA:"))
        self.fichas -= suApuesta
        print(self.fichas)
        return suApuesta

class Jugador_Computadora(jugador_cliente):
    
    
    def __init__(self, nombre, fichas = 100):
        super().__init__(nombre,fichas)
        self.personalidad = randint(1,10)#1 ==> moderado 10 ==> loco
    
    def apuesta(self):
        x = self.pensar()
        while x < self.personalidad:
            x = self.pensar() 
        apuesta = int(self.fichas * self.personalidad * x / 100)
        if apuesta == 0:
            apuesta = 1
        return apuesta
    
    def sePlanta(self):
        respuesta = False
        s = self.sumar_cartas()
        
        if s > 10:
            x = self.pensar()
            if x < self.personalidad:
                return False
            else:
                return True
        else: 
            return False
       
        return respuesta  
    
    def pensar(self):
        return randint(1,10) 

class Jugador_Croupier(Jugador):
    
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def sePlanta(self):
        return self.sumar_cartas() >= 17    

def main():
    j = Jugador("juan")
    
    j.mano.poner(Carta_poker(8,1))
    j.mano.poner(Carta_poker(1,2))
    j.mano.poner(Carta_poker(7,3))
    j.mano.poner(Carta_poker(2,4))

    print(str(j)," suma: ",j.sumar_cartas())

if __name__ == "__main__":
    main()
