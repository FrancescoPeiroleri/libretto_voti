from dataclasses import dataclass

@dataclass
class Voto:
    nome_corso: str
    punteggio: int
    data: str


    def __str__(self):
        return f"{self.nome_corso} {self.punteggio} {self.data}"


