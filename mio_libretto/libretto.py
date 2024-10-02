import voto

class libretto:

    def __init__(self):
        self._voti = []

    def add_voti(self, voti):
        if self.esisteUguale(voti) == False and self.cercaConflitto(voti) == False:
            self._voti.append(voti)
        else:
            print(f'{voti} esiste già o è in conflitto')

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

        return None

    def cercaConflitto(self, voto):
        for v in self._voti:
            if v.nome_corso == voto.nome_corso and v.punteggio != voto.punteggio:
                return True
        return False

    def copy(self):

        nuovo = libretto()
        for v in self._voti:
            nuovo.add_voti(v)

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