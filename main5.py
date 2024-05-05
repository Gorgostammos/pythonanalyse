import matplotlib.pyplot as plt

# Data for sektordiagrammet
labels = ['Ja', 'Nei']
sizes = [15, 6]  # Antall svar for hvert alternativ

# Opprette sektordiagrammet
plt.figure(figsize=(8, 8))  # Størrelsen på figuren
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Sørger for at pie er tegnet som en sirkel.

# Tilleggsfunksjoner for å forbedre diagrammet
plt.title('')
plt.show()