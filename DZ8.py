ime = input("Unesite ime: ")
def prvo_ime(ime):
    return "Dobrodošli, " + ime
druga = lambda ime: "Pozdrav, " + ime + "!"

def treca(druga):
    return druga(ime)

print(treca(druga))
