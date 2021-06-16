n = int(input("Unesite broj: "))

def parni_brojevi(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
            
for i in parni_brojevi(n):
    print("Parni broj:",i)
    
print("---------------")

def neparni_brojevi(n):
    for i in range(n):
        if i % 2 != 0:
            yield i

for i in neparni_brojevi(n):
    print("Neparni broj:",i)


    
