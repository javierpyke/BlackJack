from mazo import Mazo_blackjack
from jugador import Jugador_Croupier, Jugador_Computadora, Jugador_Humano



class BlackJack:

    def __init__(self):
        self.croupier = Jugador_Croupier("Sr Croupier")
        self.losJugadores = []
        self.elMazo = Mazo_blackjack()
        self.pozo = {}

    def agregarJugadorH(self,nombreJugador,fichas):
        jugador = Jugador_Humano(nombreJugador,fichas)
        self.losJugadores.append(jugador)
    
    def agregarJugadorB(self,nombreJugador,fichas):
        self.losJugadores.append(Jugador_Computadora(nombreJugador,fichas))
    
    def hayJugadores(self):
        return len(self.losJugadores) > 0

    def apuestas(self):
         for jug in self.losJugadores:
            print(str(jug.nombre))            
            self.pozo.update({jug.nombre:str(jug.apuesta())})

    def repartirCartas(self):        
        for jug in self.losJugadores:
            jug.mano.poner(self.elMazo.sacar())           
            jug.mano.poner(self.elMazo.sacar())
        
        self.croupier.mano.poner(self.elMazo.sacar())
        self.croupier.mano.poner(self.elMazo.sacar())

    def descartar(self):
        for jug in self.losJugadores:
            while jug.mano.hayCartas():
                self.elMazo.poner(jug.mano.sacar())
        
        while self.croupier.mano.hayCartas():
                self.elMazo.poner(self.croupier.mano.sacar())
    
    def quitar_Jugadores_sin_fichas(self):
        for jug in self.losJugadores:
            if jug.get_fichas() == 0:
                self.losJugadores.remove(jug)
    
    def jugar(self):
        self.elMazo.llenar()
        self.elMazo.mezclar()
        while self.hayJugadores():
            self.pozo={}
            print("------------------")
            print("HAGAN SUS APUESTAS")
            print("------------------")
            self.apuestas()
            print("------------------")
            print("REPARTIENDO CARTAS")
            print("------------------")
            self.repartirCartas()
            for jug in self.losJugadores:
                print(jug.nombre,"  ",str(jug.mano) , " " ,jug.sumar_cartas())
            print(self.croupier.nombre,"  ",str(self.croupier.mano)," ",self.croupier.sumar_cartas())
            for jug in self.losJugadores:
                while not jug.sePlanta():
                    jug.mano.poner(self.elMazo.sacar())
            while not self.croupier.sePlanta():
                self.croupier.mano.poner(self.elMazo.sacar())            
            self.ganar()
            self.descartar()
            self.quitar_Jugadores_sin_fichas()
            
    def ganar(self):
        blackjack = 0
        sj = 0
        sc = self.croupier.sumar_cartas()
        for jug in self.losJugadores:
            sj = jug.sumar_cartas()
            print(jug.nombre,sj," CROUPIER: ",sc)
            if sj > 21:
                    print(jug.nombre,"PIERDE")
            else:
                if sc > 21:
                    print(jug.nombre," GANA: ",int(self.pozo[jug.nombre])*2)
                    jug.fichas += int(self.pozo[jug.nombre])*2
                else:
                    if  sj < sc:
                        print(jug.nombre,"PIERDE")
                    else:
                        if sj > sc:
                            print(jug.nombre," GANA: ",int(self.pozo[jug.nombre])*2)
                            jug.fichas += int(self.pozo[jug.nombre])*2
                        else:
                            print(jug.nombre," EMPATA CON CROUPIER Y SE QUEDA CON SU APUESTA DE: " ,int(self.pozo[jug.nombre])*1)
                            jug.fichas += int(self.pozo[jug.nombre])*1


def main():
    juego = BlackJack()
    juego.agregarJugadorH("Juan",100)
    juego.agregarJugadorB("Pepe",100)
    juego.jugar()


main()