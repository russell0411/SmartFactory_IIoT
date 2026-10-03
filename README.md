Smart Factory & Industrial IoT

Ein persönliches Lernprojekt: Python lernen und gleichzeitig etwas Industrielles damit bauen.
Eine virtuelle Maschine erzeugt Sensordaten. Diese werden übertragen, gespeichert, analysiert und visualisiert. Am Ende soll ein vereinfachtes Konzept für Predictive Maintenance stehen.
Entstanden im Rahmen des Moduls Data Literacy (Hochschule Darmstadt, Maschinenbau). Mir geht es nicht um möglichst viel Code, sondern darum zu verstehen, wie Maschinenbau, Daten und IoT zusammenspielen.

Projektstruktur
Das Projekt besteht aus 10 Versionen in 3 Phasen. Jede Version wird in einem LinkedIn-Post vorgestellt und hier veröffentlicht.

Phase	Versionen	Inhalt
Simulation & Daten	V1 – V5	Maschinensimulation, Sensordaten, Zeitreihen, große Datensätze, Anomalieerkennung
Infrastruktur	V6 – V7	SQL-Datenbank, Industrial IoT mit MQTT
Intelligenz	V8 – V10	Dashboard, Machine Learning, Predictive Maintenance
Aktueller Stand:V1 und V2 sind veröffentlicht. Die weiteren Versionen folgen mit den Posts.
V2: Sensordaten und Zeitreihen
Die Simulation erzeugt 100 Messungen von drei Sensoren (Temperatur, Vibration, Strom). Bis Messung 70 läuft die Maschine normal. Danach beginnt der Verschleiß, und die Werte driften langsam nach oben.

Was das Skript macht:
Maschinenzustand ausgeben
Zeitreihe der Sensordaten erzeugen (mit Zeitstempel und Verschleiß ab Messung 70)
Datensatz mit Pandas aufbauen
Statistische Auswertung (Mittelwert, Minimum, Maximum, Standardabweichung)
Verläufe mit Matplotlib darstellen
Anomalien über feste Grenzwerte erkennen (70 °C, 3 mm/s, 12 A)
Anomaliequote und Maschinenstatus berechnen
Daten als CSV speichern und wieder einlesen
Zentrale Erkenntnis: Feste Grenzwerte schlagen erst spät an. Mit `random.seed(42)` beginnt der Verschleiß bei Messung 70, die erste Anomalie wird aber erst bei Messung 85 erkannt. Das Ergebnis gilt für diesen einen Zufallswert und ist kein Durchschnitt über viele Läufe.

Ausführen
Voraussetzungen: Python 3 sowie die Pakete `pandas` und `matplotlib`.
```bash
pip install pandas matplotlib
python machine_simulation.py
```
Durch den festen Zufallswert (`random.seed(42)`) sind die Ergebnisse bei jedem Lauf identisch und damit reproduzierbar.

Ausblick
Im weiteren Verlauf ersetzen intelligentere Verfahren die festen Grenzwerte: realistischere Simulation, Datenbank, MQTT-Übertragung, Dashboard und Machine Learning für Predictive Maintenance.

Feedback
Kommentare, Fragen und Kritik sind ausdrücklich erwünscht, am liebsten unter den LinkedIn-Posts oder als Issue in diesem Repository.
