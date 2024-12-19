#Oppgave 4.2

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

nytt_land = input("Skriv inn et land: ")
ny_hovedstad = input("Skriv inn hovedstaden til landet: ")
nytt_innbygg_tall = float(input("Skriv inn innbyggertallet til hovedstaden i millioner med desimaler: "))

new_key = nytt_land
data[new_key] = ny_hovedstad, nytt_innbygg_tall

print(f"Her følger den oppdaterte listen: {data}")