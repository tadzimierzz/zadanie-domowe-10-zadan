numbers = []

for i in range(5):
    liczba = int(input("Podaj liczbę: "))
    numbers.append(liczba)

print("Twoje liczby:", numbers)

suma = sum(numbers)

print("Suma liczb:", suma)

najwieksza = max(numbers)

print("Największa liczba:", najwieksza)

najmniejsza = min(numbers)

print("Najmniejsza liczba:", najmniejsza)

srednia = suma / len(numbers)

print("Średnia:", srednia)

parzyste = 0

for liczba in numbers:
    if liczba % 2 == 0:
        parzyste = parzyste + 1

print("Liczb parzystych:", parzyste)

duplicates = []

for liczba in numbers:
    if numbers.count(liczba) > 1:
        if liczba not in duplicates:
            duplicates.append(liczba)

print("Powtarzające się liczby:", duplicates)

bez_powtorzen = []

for liczba in numbers:
    if liczba not in bez_powtorzen:
        bez_powtorzen.append(liczba)

numbers = bez_powtorzen

print("Lista bez powtórzeń:", numbers)

squares = []

for liczba in numbers:
    kwadrat = liczba * liczba
    squares.append(kwadrat)

print("Kwadraty liczb:", squares)