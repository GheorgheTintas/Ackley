from math import exp, sqrt, cos, pi, e
from random import randint


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

    #combina populatia si fitness-ul intr-o singura structura de date
    tuplu = zip(populatie, fitness_populatie)
    #populatie_cu_fitness[0] = (populatie[0], fitness_populatie[0])
    #populatie_cu_fitness[0][1] = fitness_populatie[0]
    populatie_cu_fitness = list(tuplu)

    while len(parinti) != DIM_PARINTI:
        #alegem participantii
        participanti = []
        while len(participanti) != DIM_TURNEU:
            #alegem participant aleator
            index_participant_random = randint(len(populatie_cu_fitness))
            participant = populatie_cu_fitness[index_participant_random]
            if participant not in participanti:
                participanti.append(participant)
        #gasim invingator
        castigator = min(participanti, key=lambda participant: participant[1])
        # fiecare parinte e unic
        if castigator not in parinti:
            parinti.append(castigator)

    return parinti


def main():
    # parametri
    DIM_POPULATIE = 10
    MAX_GENERATII = 10
    MINIM, MAXIM = -5, 5
    DIM_PARINTI = 5
    DIM_TURNEU = 3

    populatie = initializeaza_populatie(DIM_POPULATIE, MINIM, MAXIM)
    fitness_populatie = calculeaza_fitness(populatie)

    for i in range(MAX_GENERATII):
        parinti = selectie(populatie, fitness_populatie, DIM_PARINTI, DIM_TURNEU)
        copii = recombinare(parinti)
        mutatie(copii)

        # actualizam populatia
        populatie = copii
        calculeaza_fitness(populatie)


if __name__ == '__main__':
    main()