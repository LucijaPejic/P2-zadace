from csv import reader
with open('rezultati.csv','r', encoding="utf8") as read_obj:
    csv_reader = reader(read_obj)
    rezultati = list(map(tuple, csv_reader))

sortirat = []
for ime,prezime,bodovi in rezultati:
    sortirat.append((prezime,ime,bodovi))
sortirat.sort(reverse=True)
print(sortirat)

ukupneOcjene = {'jedinice': 0, 'dvice': 0, 'trice': 0, 'cetvorke': 0, 'petice': 0}

for prezime,ime,bodovi in sortirat:
    if int(bodovi) > 90 and int(bodovi) <= 100:
        ukupneOcjene['petice'] += 1
    elif int(bodovi) > 80 and int(bodovi) < 90:
        ukupneOcjene['cetvorke'] += 1
    elif int(bodovi) > 65 and int(bodovi) < 80:
        ukupneOcjene['trice'] += 1
    elif int(bodovi) >= 50 and int(bodovi) < 65:
        ukupneOcjene['dvice'] += 1
    elif int(bodovi) <= 49:
        ukupneOcjene['jedinice'] += 1


print("Broj jedinica:", ukupneOcjene['jedinice'])
print("Broj dvica:", ukupneOcjene['dvice'])
print("Broj trica:", ukupneOcjene['trice'])
print("Broj četvorki:", ukupneOcjene['cetvorke'])
print("Broj petica:", ukupneOcjene['petice'])


