import matplotlib.pyplot as plt
import numpy as np

# Data for stolpediagrammet
labels = ['Svært usannsynlig', 'Usannsynlig', 'Nøytral', 'Sannsynlig', 'Svært sannsynlig']
values = [1, 5, 2, 11, 2]  # Data for gruppen

x = np.arange(len(labels))  # Label-lokasjoner
width = 0.5  # Bredden på stolpene

fig, ax = plt.subplots()
rects = ax.bar(x, values, width, label='Antall svar')

# Legg til tekst for labels, tittel og tilpassede x-aksen ticks, etc.
ax.set_xlabel('Svaralternativer')
ax.set_ylabel('Antall svar')
ax.set_title('')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Funksjon for å legge til etiketter på stolpene
def autolabel(rects):
    """Fest en tekstetikett over hver stolpe som viser dens høyde."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects)

fig.tight_layout()

plt.show()