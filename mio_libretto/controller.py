from view import View
from voto import Libretto
from voto import Voto
import flet as ft


class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Libretto()

        self.startupLibretto()
        self._model.stampa()

    def startupLibretto(self):
        v1 = Voto("Analisi 1", 25, "2020-01-22" )
        v2= Voto("Fisica 1", 19, "2024-06-29")
        v3 = Voto("Fisica 2", 22, "2023-07-5")
        self._model.add_voti(v1)
        self._model.add_voti(v2)
        self._model.add_voti(v3)

    def handleAdd(self, e):
        nameEsame = self._view._txtIn.value
        if nameEsame == "":
            self._view._lvOut.controls.append(ft.Text("Il campo nome non può essere vuoto!",
                                                      color="red"))
            self._view.update()
            return

        """
        strCfu = self._view._txtCFU.value

        try:
            intCfu = int(strCfu)
        except ValueError:
            self._view._lvOut.controls.append((ft.Text("Il campo CFU deve essere un intero.",
                                                       color="red")))
            self._view.update()
            return
        """

        punteggio = self._view._ddVoto.value

        if punteggio == None:
            self._view._lvOut.controls.append((ft.Text("Il campo punteggio va selezionato.",
                                                       color="red")))
            self._view.update()
            return

        if punteggio == "30L":
            punteggio = 30
            lode = True
        else:
            punteggio = int(punteggio)
            lode = False

        data = self._view._datePicker.value
        if data == None:
            self._view._lvOut.controls.append((ft.Text("Seleziona una data.",
                                                       color="red")))
            self._view.update()
            return

        self._model.add_voti(Voto(nameEsame, punteggio,
                                f"{data.year}-{data.month}-{data.day}"))
        self._view._lvOut.controls.append(ft.Text("Voto correttamente aggiunto.",
                                                  color="green"))
        self._view.update()
    def handlePrint(self, e):
        outList = self._model.stampaGUI()
        for elem in outList:
            self._view._lvOut.controls.append(ft.Text(elem))
        self._view.update()