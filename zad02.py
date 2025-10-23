# 2. Konwersja kilometry na mile i odwrotnie.
#    W programie wybieramy w pętli aż podamy poprawny wybór np.
#    'Podaj typ konwersji [km->mile]- 0, [mile->km]-1'.
#    Na tej podstawie wykonujemy funkcje wcześniej zdefiniowaną
#    km_mile(distance) lub mile_km(distance)

def km_mile(x):
    return x * 0.60934
def mile_km(x):
    return x * 1.60934
n=3
while n!=0 and n!=1:
    n=int(input("Podaj typ konwersji [km->mile]- 0, [mile->km]-1: "))

else:
    w=int(input("podaj wartosc"))
    if n==1:
        print(mile_km(w))
    else:
        print(km_mile(w))