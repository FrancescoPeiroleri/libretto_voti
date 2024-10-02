import voto, libretto

l1 = libretto.libretto()

v1 = voto.Voto("Analisi 1", 25, "2020-01-22" )
v2= voto.Voto("Fisica 1", 19, "2024-06-29")
v3= voto.Voto("Fisica 2", 22, "2023-07-5")

l1.add_voti(v1)
l1.add_voti(v2)
l1.add_voti(v3)

voti25 = l1.find_by_points(25)
for v in voti25:
    print(v)

v4 = voto.Voto("Analisi 1", 25, "2020-01-22" )

if l1.esisteUguale(v4) == True:
    print("Esiste già il voto")

cercato = l1.cercaPerNome("Fisica 1")
if cercato != None:
    print(cercato)

v5 = voto.Voto("Analisi 1", 24, "2020-01-22" )

if l1.cercaConflitto(v5) == True:
    print("Voto in conflitto con esame già a libretto")

l1.add_voti(v4)
l1.add_voti(v5)

migliorato = l1.librettoMigliorato()
