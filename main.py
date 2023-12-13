from math import exp, sqrt, cos, pi, e
from random import randint, uniform


def genereaza_individ(MINIM, MAXIM):
    x = randint(MINIM, MAXIM)
    y = randint(MINIM, MAXIM)
    individ = [x, y]
    return individ


def initializeaza_populatie(DIM_POPULATIE, MINIM, MAXIM):
    populatie = []
    for i in range(DIM_POPULATIE):
        individ = genereaza_individ(MINIM, MAXIM)
        populatie.append(individ)
    return populatie


def ackley(individ):
    x = individ[0]
    y = individ[1]
    z = -20.0 * exp(-0.2 * sqrt(0.5 * (x ** 2 + y ** 2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + e + 20
    return z


def calculeaza_fitness(populatie):
    fitness_populatie = []
    for individ in populatie:
        z = ackley(individ)
        fitness_populatie.append(z)
    return fitness_populatie


def selectie(populatie, fitness_populatie, DIM_PARINTI, DIM_TURNEU):
    parinti = []

    # combina populatia si fitness-ul intr-o singura structura de date
    tuplu = zip(populatie, fitness_populatie)
    # populatie_cu_fitness[0] = (populatie[0], fitness_populatie[0])
    # populatie_cu_fitness[0][1] = fitness_populatie[0]
    populatie_cu_fitness = list(tuplu)

    while len(parinti) != DIM_PARINTI:
        # alegem participantii
        participanti = []
        while len(participanti) != DIM_TURNEU:
            # alegem participant aleator
            index_participant_random = randint(0, len(populatie_cu_fitness) - 1)
            participant = populatie_cu_fitness[index_participant_random]
            participanti.append(participant)

        # gasim invingator
        tuplu = min(participanti, key=lambda participant: participant[1])
        # tuplu[0] = individ, tuplu[1] = fitness
        castigator = tuplu[0]
        parinti.append(castigator)
    return parinti


def recombinare(parinti):
    copii = []

    for i in range(len(parinti)):
        index_parinte1 = randint(0, len(parinti) - 1)
        index_parinte2 = randint(0, len(parinti) - 1)

        parinte1 = parinti[index_parinte1]
        parinte2 = parinti[index_parinte2]

        # print(parinte1, parinte2)

        x_parinte1 = parinte1[0]
        y_parinte1 = parinte1[1]

        x_parinte2 = parinte2[0]
        y_parinte2 = parinte2[1]

        x_copil = (x_parinte1 + x_parinte2) / 2
        y_copil = (y_parinte1 + y_parinte2) / 2

        copil = [x_copil, y_copil]
        copii.append(copil)

    return copii


def mutatie(copii, RATA_MUTATIE):
    for copil in copii:
        for i in range(len(copil)):
            numar_random = randint(0, 99)
            if numar_random < RATA_MUTATIE:
                cantitate_random = uniform(-1, 1)
                copil[i] += cantitate_random


def gaseste_index_best(fitness_populatie):
    # cautam elementul minim
    fitness_minim = min(fitness_populatie)
    # cautam indexul elementului minim
    index_fitness_minim = fitness_populatie.index(fitness_minim)
    return index_fitness_minim


def main():
    # parametri
    DIM_POPULATIE = 50
    MAX_GENERATII = 1000
    MINIM, MAXIM = -50, 50  # capete domeniu functie Ackley
    DIM_PARINTI = 25 # 0 < DIM_PARINTI <= DIM_POPULATIE
    DIM_TURNEU = 3
    RATA_MUTATIE = 5

    populatie = initializeaza_populatie(DIM_POPULATIE, MINIM, MAXIM)
    fitness_populatie = calculeaza_fitness(populatie)

    # gasim cea mai buna solutie din populatia initiala
    index_best = gaseste_index_best(fitness_populatie)
    solutie_best = populatie[index_best]
    fitness_best = fitness_populatie[index_best]

    for i in range(MAX_GENERATII):
        parinti = selectie(populatie, fitness_populatie, DIM_PARINTI, DIM_TURNEU)
        copii = recombinare(parinti)
        mutatie(copii, RATA_MUTATIE)

        # actualizam populatia
        populatie = copii
        fitness_populatie = calculeaza_fitness(populatie)

        # cautam cel mai bun in generatia curenta
        index_best = gaseste_index_best(populatie)
        fitness_best_generatie_curenta = fitness_populatie[index_best]
        # actualizam cel mai bun daca e mai bun decat cel mai bun ever
        if fitness_best_generatie_curenta < fitness_best:
            solutie_best_generatie_curenta = populatie[index_best]
            solutie_best = solutie_best_generatie_curenta

    print("Cea mai buna solutie: ", solutie_best, ", fitness: ", fitness_best)


if __name__ == '__main__':
    main()