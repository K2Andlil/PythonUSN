fors_elbil = 5000 #Forsikring
fors_bensinbil = 7500 #Forsikring
year_km = 10000
tra_fors_per_year = 8.38*365 #Trafikk forsikring per år
drivstoff_bensinbil = 1*year_km #Kostnad drivstoff bensinbil per år
kwh_per_km = 0.2
kr_per_kwh = 2
kr_per_km_elbil = kr_per_kwh*kwh_per_km
drivstoff_elbil = kr_per_km_elbil*year_km #Kostnad elbil drovistoff per år
bom_per_km_elbil = 0.1*year_km #Årlig bom kostnad elbil
bom_per_km_bensinbil = 0.3*year_km #Årlig bom kostnad elbil
kostnad_bensinbil_per_year = fors_bensinbil + tra_fors_per_year + drivstoff_bensinbil + bom_per_km_bensinbil
kostnad_elbil_per_year = fors_elbil + tra_fors_per_year + drivstoff_elbil + bom_per_km_elbil
differanse = kostnad_bensinbil_per_year - kostnad_elbil_per_year
print(f"Bensinbilen koster {kostnad_bensinbil_per_year},- kroner per år og elbilen koster {kostnad_elbil_per_year},- kroner per år")
print(f"Elbilen er altså {differanse},- kroner billigere i året")

