def unazad(n):
     if n == "":
        return n
     else:
        return unazad(n[1:]) + n[0]
        
n = input("Unesite rečenicu: ")

print(unazad(n))
