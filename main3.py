import matplotlib.pyplot as plt

# Data for gruppe_1
spørsmal_6_svar = [
    4,4,3,3,4,3,3,
    4,5,4,4,4,3,3,
    4,2,3,5,4,5,5

]
spørsmal_6_antall_personer_som_valgte_samme_svar = {

    1: 0,
    2: 1,
    3: 7,
    4: 9,
    5: 4
}

# Data for gruppe_2
spørsmal_13_svar_svar = [
    5,4,3,3,
    3,4,3,3,
    5,4,4,4,
    4,3,4,3,
    3,5,4,5,5

]
spørsmal_13_antall_personer_som_valgte_samme_svar = {
    1: 0,
    2: 0,
    3: 8,
    4: 8,
    5: 5
}

# Alternativene for spørsmålet
alternativer = list(range(1, 6))

# Antall personer som valgte hvert alternativ for hver gruppe
spørsmal_6_antall = [spørsmal_6_antall_personer_som_valgte_samme_svar[alternativ] for alternativ in alternativer]
spørsmal_13_antall = [spørsmal_13_antall_personer_som_valgte_samme_svar[alternativ] for alternativ in alternativer]

# Beregning av gjennomsnittslinjen

# Plotting
plt.plot(alternativer, spørsmal_6_antall, marker='o', label='Før at de hører talen ')
plt.plot(alternativer, spørsmal_13_antall, marker='o', label='Etter at de hørte talen ')
plt.xlabel('Svaralternativer')
plt.ylabel('Antall svar')
plt.title('')
plt.xticks(alternativer)  # Setter aksetikettene til å være alternativene
plt.legend()
plt.grid(True)
plt.show()