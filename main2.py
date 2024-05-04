import matplotlib.pyplot as plt

# Data for gruppe_1
spørsmal_4_svar = [
    4,5,3,4,4,3,2,2,3,4,3,
    4,2,4,3,4,2,5,5,4,4
]
spørsmal_4_antall_personer_som_valgte_samme_svar = {

    1: 0,
    2: 4,
    3: 5,
    4: 9,
    5: 3
}

# Data for gruppe_2
spørsmal_11_svar_svar = [
    5,4,3, 4, 4, 3,
    5, 3,2, 4, 3, 4,
    3, 3,4, 4, 3, 5,
    5, 5, 4
]

spørsmal_11_antall_personer_som_valgte_samme_svar = {
    1: 0,
    2: 1,
    3: 7,
    4: 8,
    5: 5
}

# Alternativene for spørsmålet
alternativer = list(range(1, 6))

# Antall personer som valgte hvert alternativ for hver gruppe
spørsmal_4_antall = [spørsmal_4_antall_personer_som_valgte_samme_svar[alternativ] for alternativ in alternativer]
spørsmal_11_antall = [spørsmal_11_antall_personer_som_valgte_samme_svar[alternativ] for alternativ in alternativer]

# Beregning av gjennomsnittslinjen

# Plotting
plt.plot(alternativer, spørsmal_4_antall, marker='o', label='Før at de hører talen ')
plt.plot(alternativer, spørsmal_11_antall, marker='o', label='Etter at de hørte talen ')
plt.xlabel('Svat alternativer')
plt.ylabel('Antall personer')
plt.title('Sammenligningen av svardatene før og etter å ha hørt talen')
plt.xticks(alternativer)  # Setter aksetikettene til å være alternativene
plt.legend()
plt.grid(True)
plt.show()