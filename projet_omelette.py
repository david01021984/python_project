#import libraries nécessaires
import time 
import pygame   

#definition de mes classes 

class Panier():
# Panier: Représente un panier avec un type (par défaut "Panier") et un contenu (une liste d'objets, par défaut vide)
    def __init__(self,type="Panier",contenu=None):
        self.type = type 
        self.contenu = [] if contenu is None else contenu
    
    def MontrerContenu(self):
        print(f"Le panier contient : {panier_1.contenu}") 
        
class Personnage():
# Personnage: Représente un personnage avec un nom, une quantité d'argent, un lieu actuel, 
# et des objets dans ses mains droite et gauche

    def __init__(self, nom, argent:float, lieu = None, main_droite=None, main_gauche=None):
        self.nom = nom
        self.lieu = lieu
        self.argent = argent
        self.main_droite = [] if main_droite is None else main_droite
        self.main_gauche = [] if main_gauche is None else main_gauche
    
    def seDeplacer(self, destination):
        self.lieu = destination.nom
        destination.personnes.append(self.nom)
        print(f"{self.nom} est arrivé à {destination.nom}")
    
    def payerArticle(self, article):
        self.argent -= article.prix
    
    def couper(self, ingredient, outil):
        ingredient.etat = "coupé"
        print(f"Je decoupe {ingredient.nom} avec {outil.nom}!")
    
    def attraper(self,panier):
        for i in panier.contenu: 
            self.main_gauche.append(i)
            print(f"{self.nom} a attrapé en main {i}")
        panier.contenu = []
    
    def rendrePanier(self):
        print(f"Merci {self.nom} d'avoir utiliser un panier réutilisable à vous!")
        print("La planète vous en remercie... Beau geste!!!")

    def localiser(self):
        print(f"{self.nom} se trouve à : {self.lieu}")

    def detenirEnMain(self):
        print(f"{self.nom} a en main les articles suivants : {self.main_gauche}")

    def avoirEnPoche(self):
        print(f"{david.nom} a {david.argent} euro(s) en poche")

class Lieu():
# Lieu: Représente un lieu avec un nom et une liste de personnes présentes
    def __init__(self, nom, personnes = None):
        self.nom = nom
        self.personnes = [] if personnes is None else personnes


class Outil():
# Outil: Représente un outil avec un nom et une action associée
    def __init__(self,nom,action):
        self.nom = nom
        self.action = action
        
class Ingredient():
# Ingredient: Représente un ingrédient avec un nom, un prix, un état (par défaut "Entier").
    def __init__(self, nom, prix:float, etat = "Entier"):
        self.nom = nom
        self.prix = prix
        self.etat = etat 

    def __str__(self):
        return self.nom
    
    def __repr__(self):
        return self.nom

class Shop(Lieu):
# Shop (Magasin): Hérite de la classe Lieu et représente un magasin avec des paniers, des ingrédients, et des personnes.
    def __init__(self,nom, personnes=None, paniers=None,ingredients=None):
        super().__init__(nom,personnes=None)
        self.paniers = [] if paniers is None else paniers
        self.ingredients = [] if ingredients is None else ingredients

class Bol():
# Bol: Représente un bol avec un contenu (une liste d'objets, par défaut vide).
    def __init__(self,contenu=None):
        self.contenu = [] if contenu is None else contenu

    def battre(self,nom_melange):
        new_ingr = Ingredient(nom_melange,0,"cru")
        self.contenu = nom_melange
        return new_ingr
    
    def nettoyer(self):
        self.contenu = []
        time.sleep(2)
        print("Ton bol est désormais vide et nettoyé!")

class Poelle():
# Poelle: Représente une poêle avec un contenu (une liste d'objets, par défaut vide).
    def __init__(self, contenu = None):
        self.contenu = [] if contenu is None else contenu
        pygame.mixer.init()  # Initialize the mixer
        pygame.mixer.music.load("pan_noise.wav") 
    
    def cuire(self,ingredient):
        time.sleep(1)
        print(f"Cuisson de notre {ingredient.nom} en cours...")
        pygame.mixer.music.play()
        time.sleep(4)
        pygame.mixer.music.stop()
        ingredient.etat = "cuit"
        print(f"Notre {ingredient.nom} est cuite")
    
    
# instanciation des objects utilisés dans le prog
# Le code crée des instances de lieux (maison, épicerie), d'outils (couteau), 
# d'ingrédients (œuf, lait, fromage, sel, poivre), de paniers, de bols, et d'une poêle. 


maison = Lieu("Maison")
epicerie=Shop("Epicerie",["L'épicier"])
mon_couteau = Outil("Couteau","Couper")
 
david = Personnage("David",150)
ma_poelle = Poelle()
mon_bol=Bol()

oeuf = Ingredient("Oeuf",2.5)
lait = Ingredient("Lait",1.5,"liquide")
fromage = Ingredient("Fromage",3,"rapé")

sel = Ingredient("Sel",1)
poivre = Ingredient("Poivre",1.3)

panier_1 = Panier(contenu=[oeuf,lait,fromage])
panier_2 = Panier(contenu=[sel,poivre])

# print de qq valeurs pour voir clair
'''
print(mon_bol.contenu)
print(ma_poelle.contenu)
print(david.argent)
print(david.lieu)
'''

# Ensuite, il simule une série d'actions de David, telles que se déplacer, attraper un panier, 
# payer des articles, retourner à la maison, couper des ingrédients, battre des ingrédients dans un bol, 
# et enfin cuire dans une poêle

def main():
# La fonction main() appelle ces actions pour simuler le déroulement du scénario.
# Le résultat final est la création d'une omelette dans la poêle à partir des ingrédients dans le bol.
    david.localiser()
    
    david.seDeplacer(maison)
    
    david.localiser()

    david.seDeplacer(epicerie)
   
    panier_1.MontrerContenu()
    
    david.detenirEnMain()

    david.attraper(panier_1)

    david.detenirEnMain()

    david.avoirEnPoche()

    for i in david.main_gauche :
        print(i)
        david.payerArticle(i)

    david.avoirEnPoche()

    david.seDeplacer(maison)

    print(david.lieu)

    for i in david.main_gauche:
        mon_bol.contenu.append(i)
    david.main_gauche = []
    
    print(f"Dans mon bol y a : {mon_bol.contenu}")
    
    david.detenirEnMain()


    david.seDeplacer(epicerie)
    david.rendrePanier()
    david.seDeplacer(maison)

    for i in mon_bol.contenu:
        if i.etat == "Entier":
            david.couper(i, mon_couteau)
            print(i.etat)

    omelette = mon_bol.battre("omelette")
    print(f"Dans mon bol y a {mon_bol.contenu}")
    #Je passe les ingredients de mon bol a ma poelle...
    ma_poelle.contenu = mon_bol.contenu
     
    mon_bol.nettoyer()

    print(f"Dans ma poelle now j'ai : {ma_poelle.contenu}")
    
    print(omelette.etat)
    ma_poelle.cuire(omelette)
    #vérif etat 
    print(omelette.etat)


main()



