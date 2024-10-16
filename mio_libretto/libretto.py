import operator

import voto

class Libretto:

    def __init__(self):
        self._voti = []

    def add_voti(self, voti):
        if self.esisteUguale(voti) == False and self.cercaConflitto(voti) == False:
            self._voti.append(voti)
        else:
            raise ValueError(f'{voti} esiste già o è in conflitto')

    def find_by_points(self, points):

        corsi = []
        for voto in self._voti:
            if voto.punteggio == points:
                corsi.append(voto)

        return corsi

    def esisteUguale(self, voto):
        for v in self._voti:
            if v.nome_corso == voto.nome_corso and v.punteggio == voto.punteggio:
                return True

        return False

    def  cercaPerNome(self, nome):
        for v in self._voti:
            if v.nome_corso == nome:
                return v
        raise ValueError(f"Esame '{v.nome_corso}' non presente nel libretto")


    def cercaConflitto(self, voto):
        for v in self._voti:
            if v.nome_corso == voto.nome_corso and v.punteggio != voto.punteggio:
                return True
        return False

    def copy(self):

        nuovo = libretto()
        for v in self._voti:
            nuovo.add_voti(v.copy())

        return nuovo





    def librettoMigliorato(self):

        migliorato = self.copy()

        for v in migliorato._voti:
            if 18 <= v.punteggio <= 23:
                v.punteggio += 1
            elif 24 <= v.punteggio <= 28:
                v.punteggio += 2
            elif v.punteggio == 29:
                v.punteggio = 30

        return migliorato

    def stampa(self):
        for v in self._voti:
            print(v)

    def ordinaPerEsame(self):

        self._voti.sort(key=operator.attrgetter('nome_corso'))

    def ordinaPerVoto(self):
        self._voti.sort(key=lambda x: x.punteggio, reverse=True)

    def creaOrdinatoEsame(self):
        nuovo = self.copy()
        nuovo.ordinaPerEsame()
        return nuovo

    def creaOrdinatoVoto(self):
        nuovo = self.copy()
        nuovo.ordinaPerVoto()
        return nuovo

    def cancella_inferori(self, punteggio):
        #metodo remove itera la lista gni volta, anche se c'è un for
        #metodo pop non va bene, vado a lavorare su una lista su cui sto iterando, ogni volta che cancello si aggiornano gli indici, facendomi perdere dei dati
        #soluzione: creo una copia (malino) o costruisco nuova lista con ciò da mantenere

        voti_nuovi = []
        for v in self._voti:
            if v.punteggio >= punteggio:
                voti_nuovi.append(v)

        voti_nuovi =  [ v for v in self._voti if v.punteggio >= punteggio]

        self._voti = voti_nuovi

