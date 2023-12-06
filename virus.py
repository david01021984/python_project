'''
Problème: Simulation d'évolution d'une infection virale

Vous devez créer un programme en Python pour simuler l'évolution d'une infection virale 
sur une population de 11 500 000 personnes pendant une année (365 jours). 
Le modèle de simulation est basique et utilise une formule simple.

Initialisez le nombre de personnes infectées le premier jour à 100.

Utilisez la formule suivante pour calculer le nombre de personnes infectées chaque jour,
en tenant compte des rencontres quotidiennes :

nouveau_infectes = PT * infectes_jour_precedent * (population / rencontres_par_jour)

infectes_jour_actuel = infectes_jour_precedent + nouveau_infectes

où PT vaut 0.01, PG vaut 0.05, et le nombre de rencontres par jour est initialement 10.

Du jour 30 au jour 75 (inclus), pendant une période de confinement, le nombre de rencontres 
par jour devient 3 au lieu de 10.

Les scientifiques doivent pouvoir entrer le numéro d'un jour (de 1 à 365), 
et le programme affiche le nombre de personnes contaminées ce jour-là. 
S'ils entrent "0", le programme passe à la suite. Le calcul du nombre de personnes 
infectées n'est effectué qu'une seule fois pour toute l'année.

Pour obtenir plus de points :
Affichez le nombre moyen de personnes infectées par jour et le nombre moyen de nouvelles 
infections par jour sur l'ensemble de l'année.
Indiquez si la population guérira complètement, sera complètement infectée ou partiellement infectée.
Affichez le numéro du jour du premier pic du nombre de personnes infectées.

'''

def newInfected(_inf,_pop,_rpj):
    PT = 0.01
    PG = 0.05
    niag = _inf * (1-PG)
    return niag + (_pop - niag) * _rpj * niag / _pop * PT

def display(_inf):
    while True:
        day = int(input("Enter the day you want to check or -0- to quit: "))
        if day != 0:
            print(_inf[day-1])
        elif day == 0 :
            break

def completeEvolution(_pop,_inf,_maxdays):
    for i in range (0,_maxdays):
        match i:
            case x if x >= 30 and x < 75:
                nv_inf = round(newInfected(_inf[i],_pop,3),2)
                _inf.append(nv_inf)
            case _:
                nv_inf = round(newInfected(_inf[i],_pop,10),2)
                _inf.append(nv_inf)
    #print(_inf)

def picInfection(_inf):
    max_value = max(_inf)
    index_max = _inf.index(max_value)
    print(f"La valeur max est : {max_value} et tombe le {index_max}e jour!")

def averageContamination(_inf):
    return round(sum(_inf)/len(_inf),2)

def pronosticEndOfHumanity():
    print("Pas besoin de python pour ça, à ce rythme là on va tous être contaminé...")
    

def main():            
    population = 11500000
    max_days = 365
    infected = [100]
    completeEvolution(population,infected,max_days)
    display(infected)
    picInfection(infected)
    print(f"La moyenne de personne contaminée par jour est : {averageContamination(infected)}")
    pronosticEndOfHumanity()

main()
