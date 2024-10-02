from dataclasses import dataclass, field


@dataclass(order=True)
class Voto:
    nome_corso: str
    punteggio: int
    data: str = field(compare=False)


    def __str__(self):
        return f"{self.nome_corso} {self.punteggio} {self.data}"


    def copy(self):
        return Voto(self.nome_corso, self.punteggio, self.data)

