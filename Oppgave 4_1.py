# Oppgave 4.1

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

land = input("Skriv inn et land: ")
key = data[land]
print(f"{key[0]} er hovedstaden i {land} og det er {key[1]} mill. innbyggere i {key[0]}.")