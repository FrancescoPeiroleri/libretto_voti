import datetime

import flet as ft

class View(object):
    def __init__(self, page):
        self._page = page

        self._titolo = None
        self._datePicker = None

    def loadAll(self):
        self._titolo = ft.Text("Il mio libretto voti ++", color='blue', size=24, text_align=ft.TextAlign.CENTER)

        # row1

        self._txtIn = ft.TextField(label="nome esame", width=300)

        self._ddVoto = ft.Dropdown(label="voto", width=100)
        self._fillddVoto()

        self._datePicker = ft.DatePicker(
            first_date=datetime.datetime(2022, 11, 1),
            last_date=datetime.datetime(2025, 10, 31)
        )

        self._page.overlay.append(self._datePicker)

        self._btnCalendar = ft.ElevatedButton("Pick date",
                                              icon=ft.icons.CALENDAR_MONTH,
                                              on_click=lambda _: self._datePicker.pick_date())

        self._row1 = ft.Row( [self._txtIn, self._ddVoto, self._btnCalendar] ,alignment=ft.MainAxisAlignment.CENTER)

        #row2

        self._btnAdd = ft.ElevatedButton(text="add", on_click= self._controller.handleAdd)
        self._btnPrint = ft.ElevatedButton(text="print", on_click= self._controller.handlePrint)

        self._row2 = ft.Row([self._btnAdd, self._btnPrint], alignment=ft.MainAxisAlignment.CENTER)

        #row3

        self._lvOut = ft.ListView()
        self._page.add(self._titolo, self._row1, self._row2, self._lvOut)


    def setController(self, controller):
        self._controller = controller

    def _fillddVoto(self):
        for i in range(18, 30):
            self._ddVoto.options.append(ft.dropdown.Option(str(i)))

        self._ddVoto.options.append(ft.dropdown.Option("30L"))

    def update(self):
        self._page .update()