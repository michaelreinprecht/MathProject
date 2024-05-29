import pandas as pd
import numpy as np
from tabulate import tabulate


# Funktion zum Laden und Anzeigen zufälliger Datensätze sowie zur Berechnung des Mittelwerts
def display_random_samples_and_mean(file_path, n):
    # CSV-Datei einlesen
    data_df = pd.read_csv(file_path)

    # Anzahl der zufälligen Datensätze sicherstellen, dass n <= Anzahl der Zeilen in der CSV-Datei ist
    n = min(n, len(data_df))

    # Zufällige Datensätze auswählen
    random_samples = data_df.sample(n=n)

    # Ausgabe der zufälligen Datensätze in tabellarischer Form mit tabulate
    print("Zufällige Datensätze:")
    print(tabulate(random_samples, headers='keys', tablefmt='pretty'))

    # Mittelwert der ausgewählten Datensätze berechnen
    mean_values = random_samples["Successful_Missions"].mean()

    # Ausgabe der Mittelwerte
    print("\nMittelwert der successful missions dieser Stichprobe:")
    print(mean_values)




# Zufällige Datensätze anzeigen und deren Mittelwerte berechnen
display_random_samples_and_mean("../missions_per_year.csv", 10)
