import pandas as pd
import matplotlib.pyplot as plt

# Daten aus der CSV-Datei importieren
data = pd.read_csv('salary_data.csv')

# Die unabhängige Variable (Monat) und abhängige Variable (Umsatz) auswählen
X = data['Monat'].values
Y = data['Umsatz'].values

# Berechnung der Mittelwerte von X und Y
mean_x = sum(X) / len(X)
mean_y = sum(Y) / len(Y)

# Berechnung der Regressionskoeffizienten
numerator = sum((X - mean_x) * (Y - mean_y))
denominator = sum((X - mean_x) ** 2)

b1 = numerator / denominator
b0 = mean_y - b1 * mean_x

# Lineare Regression durchgeführt, b0 ist der y-Achsenabschnitt und b1 ist die Steigung

# Vorhersagen für zukünftige Monate
future_months = [11, 12, 13]
future_Y_pred = [b0 + b1 * x for x in future_months]

# Streudiagramm erstellen
plt.scatter(X, Y, label='Umsatz')
plt.plot(X, [b0 + b1 * x for x in X], color='red', label='Lineare Regression')
plt.plot(future_months, future_Y_pred, color='green', linestyle='--', marker='o', markersize=8, label='Prognose')
plt.xlabel('Monat')
plt.ylabel('Umsatz')
plt.title('Umsatzprognose')
plt.legend()

# Das Diagramm als Bild speichern
plt.savefig('umsatzprognose.png')

# Das Diagramm anzeigen
plt.show()

# Anzeige der Prognosen für die zukünftigen Monate
for month, predicted_sales in zip(future_months, future_Y_pred):
    print(f'Prognose für Monat {month}: {predicted_sales}')
