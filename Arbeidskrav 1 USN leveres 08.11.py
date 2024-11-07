#Lager teller for elbil og bensinbil
el_bil = 0
bensin_bil = 0

#Lager variabler
dag = 365
årlig_kjørelengde = 20000

#Pris på forsikring
forsikring_el = 5000
forsikring_bensin = 7500

#Bomavgift
bomavgift_el = 0.1 * årlig_kjørelengde
bomavgift_bensin = 0.3 * årlig_kjørelengde

#Trafikkforsikring
trafikkforsikring = dag * 8.38 
#print(trafikkforsikring)

#Drivstoffbruk elbil
forbruk_kWh = 0.2 * årlig_kjørelengde
drivstoff_el = 2 * forbruk_kWh
print(drivstoff_el)


#Drivstoffbruk bensinbil
drivstoff_bensin = 1 * årlig_kjørelengde

#Regner ut årlig utgifter for elbil og bensinbil
el_bil = bomavgift_el + drivstoff_el + forsikring_el + trafikkforsikring
print("Hvis årlig kjørelengde er", årlig_kjørelengde, "vil de totale utgiftene for elbil være:", el_bil, "kroner")

bensin_bil = bomavgift_bensin + drivstoff_bensin + forsikring_bensin + trafikkforsikring
print("Hvis årlig kjørelengde er", årlig_kjørelengde, "vil de totale utgiftene for bensinbil være:", bensin_bil, "kroner")

#Kostnadsdifferanse
kostnads_diff = bensin_bil - el_bil
print("Du sparer", kostnads_diff, "kroner på å kjøpe elbil")