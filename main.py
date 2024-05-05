import matplotlib.pyplot as plt

# Data for gruppe_1
spørsmal_3_svar = [
    3,4,3,4,3,5,4,3,4,2,4,3,2,4,3,3,2,5,4,4,5
]
spørsmal_3_antall_personer_som_valgte_samme_svar = {
    1: 0,
    2: 3,
    3: 7,
    4: 8,
    5: 3
}

# Data for gruppe_2
spørsmal_9_svar_svar = [
    4,4,3,4,
    4,4,4,3,
    4,2,4,3,
    4,4,4,2,
    2,5,4,5,5
]

spørsmal_9_antall_personer_som_valgte_samme_svar = {
    1: 0,
    2: 3,
    3: 3,
    4: 12,
    5: 3
}

# Alternativene for spørsmålet
alternativer = list(range(1, 6))

# Antall personer som valgte hvert alternativ for hver gruppe
spørsmal_3_antall = [spørsmal_3_antall_personer_som_valgte_samme_svar[alternativ] for alternativ in alternativer]
spørsmal_9_antall = [spørsmal_9_antall_personer_som_valgte_samme_svar[alternativ] for alternativ in alternativer]

# Beregning av gjennomsnittslinjen

# Plotting
plt.plot(alternativer, spørsmal_3_antall, marker='o', label='Før at de hører talen ')
plt.plot(alternativer, spørsmal_9_antall, marker='o', label='Etter at de hørte talen ')
plt.xlabel('Svar alternativer')
plt.ylabel('Antall Deltaker')
plt.title('')
plt.xticks(alternativer)  # Setter aksetikettene til å være alternativene
plt.legend()
plt.grid(True)
plt.show()