#================================= 
# SMART FACTORY - MASCHINENSIMULATION  
# Block 1: Maschinenzustand  
#================================= 
 
# Betriebsdaten der Maschine  
Temperatur = 65.0 
Drehzahl = 1500 
Strom = 10.5 
Vibration = 2.0 
Druck = 5.0  
 
# Maschinenzustand anzeigen  
print("=== MASCHINENZUSTAND ===") 
print("Temperatur:", Temperatur, "°C") 
print("Drehzahl:", Drehzahl, "U/min") 
print("Strom:", Strom, "A") 
print("Vibration:", Vibration, "mm/s") 
print("Druck:", Druck, "bar") 
 
# ========================================== 
# Block 2: Zeitachse der Sensordaten 
# ========================================== 
 
import random 
from datetime import datetime, timedelta 
 
messdaten = [] 
 
# Startzeit der Simulation 
startzeit = datetime.now() 
 
for messung in range(100): 
 
    # Zeitstempel erzeugen 
    zeit = startzeit + timedelta(seconds=messung) 
 
    # Normalbetrieb 
    temperatur = random.uniform(64.0, 66.0) 
    vibration = random.uniform(1.8, 2.2) 
    strom = random.uniform(10.0, 11.0) 
 
    # Ab Messung 70: Maschine beginnt sich zu verschlechtern 
    if messung >= 69: 
        alterungsfaktor = messung - 68 
 
        temperatur += alterungsfaktor * 0.3 
        vibration += alterungsfaktor * 0.05 
        strom += alterungsfaktor * 0.08 
 
    messdaten.append({ 
        "Zeit": zeit, 
        "Messung": messung + 1, 
        "Temperatur": round(temperatur, 2), 
        "Vibration": round(vibration, 2), 
        "Strom": round(strom, 2) 
    }) 
     
# ================================== 
# Block 3: Datensatz mit Pandas 
# ================================== 
 
import pandas as pd  
 
daten = pd.DataFrame(messdaten) 
 
print("\n=== DATENSATZ ===") 
print(daten.head()) 
 
print("\n=== DATENINFORMATIONEN ===") 
print(daten.info()) 
 
# ========================================== 
# Block 4: Erste Datenanalyse 
# ========================================== 
 
print("\n=== STATISTISCHE ANALYSE ===") 
 
print("\nDurchschnittswerte:") 
print(daten[["Temperatur", "Vibration", "Strom"]].mean()) 
 
print("\nMinimalwerte:") 
print(daten[["Temperatur", "Vibration", "Strom"]].min()) 
 
print("\nMaximalwerte:") 
print(daten[["Temperatur", "Vibration", "Strom"]].max()) 
 
print("\nStandardabweichung:") 
print(daten[["Temperatur", "Vibration", "Strom"]].std()) 
 
# ========================================== 
# Block 5: Datenvisualisierung 
# ========================================== 
 
import matplotlib.pyplot as plt 
 
# Figure 1: Temperatur 
plt.figure(1) 
plt.plot(daten["Messung"], daten["Temperatur"]) 
plt.xlabel("Messung") 
plt.ylabel("Temperatur [°C]") 
plt.title("Temperaturverlauf der Maschine") 
 
# Figure 2: Vibration 
plt.figure(2) 
plt.plot(daten["Messung"], daten["Vibration"]) 
plt.xlabel("Messung") 
plt.ylabel("Vibration [mm/s]") 
plt.title("Vibrationsverlauf der Maschine") 
 
# Figure 3: Strom 
plt.figure(3) 
plt.plot(daten["Messung"], daten["Strom"]) 
plt.xlabel("Messung") 
plt.ylabel("Strom [A]") 
plt.title("Stromverlauf der Maschine") 
 
# Alle drei Figuren gleichzeitig anzeigen 
plt.show() 
 
# ========================================== 
# Block 6: Automatische Anomalieerkennung 
# ========================================== 
 
# Grenzwerte definieren 
temperatur_grenzwert = 70.0 
vibration_grenzwert = 3.0 
strom_grenzwert = 12.0 
 
# Anomalien erkennen 
daten["Anomalie"] = ( 
    (daten["Temperatur"] > temperatur_grenzwert) | 
    (daten["Vibration"] > vibration_grenzwert) | 
    (daten["Strom"] > strom_grenzwert) 
) 
 
print("\n=== ANOMALIEERKENNUNG ===") 
print(daten[daten["Anomalie"]]) 
 
# ========================================== 
# Block 7: Anomalieauswertung und Maschinenstatus 
# ========================================== 
 
# Anzahl der anomalen Messungen 
anzahl_anomalien = daten["Anomalie"].sum() 
 
# Anzahl der normalen Messungen 
anzahl_normal = len(daten) - anzahl_anomalien 
 
# Anomaliequote berechnen 
anomaliequote = (anzahl_anomalien / len(daten)) * 100 
 
# Maschinenstatus bestimmen 
if anzahl_anomalien > 0: 
    maschinenstatus = "WARNUNG" 
else: 
    maschinenstatus = "OK" 
 
# Ergebnisse anzeigen 
print("\n=== MASCHINENSTATUS ===") 
print("Normale Messungen:", anzahl_normal) 
print("Anomale Messungen:", anzahl_anomalien) 
print("Anomaliequote:", round(anomaliequote, 1), "%") 
print("Status:", maschinenstatus) 
 
# ========================================== 
# Block 8: Daten als CSV speichern 
# ========================================== 
 
dateiname = "maschinen_daten.csv" 
 
daten.to_csv(dateiname, index=False) 
 
print("\n=== DATENSPEICHERUNG ===") 
print("Datensatz wurde gespeichert als:", dateiname) 
 
# ========================================== 
# Block 9: CSV wieder einlesen 
# ========================================== 
 
daten_neu = pd.read_csv("maschinen_daten.csv") 
 
print("\n=== CSV WIEDER EINGELESEN ===") 
print(daten_neu.head()) 
 
print("\nAnzahl der Messungen:", len(daten_neu)) 
print("Anzahl der Spalten:", len(daten_neu.columns)) 