'''
Projet Omelette

Créez une classe Personnage avec les propriétés et méthodes suivantes :
 - nom (str)
 - lieu (str)
 - argent (float)
 - main_droite (list)
 - main_gauche (list)
 - se_deplacer(lieu) (méthode)
 - payer_article(article) (méthode)
 - couper(ingredient, outil) (méthode)

Créez une classe Lieu "Maison" avec les propriétés :
 - nom: 'maison'
 - personnes (list, tableau des personnes présentes dans la maison)

Créez une classe Outil "Couteau" pour découper les ingrédients achetés avec les propriétés :
 - nom (str)
 - action (str) avec la valeur initiale 'entier'

Créez une classe Ingrédient pour les produits à mettre dans le magasin :
- nom (str)
- etats (list de str) avec les valeurs 'entier', 'coupé', 'moulu'
- prix (float)

Créez une classe Lieu "Epicerie" avec les propriétés :
 - nom (str)
 - personnes (list, tableau des personnes présentes dans l'épicerie)
 - paniers (list d'objets "Panier" avec une propriété "type" égale à "panier" et le contenu du panier, égal à une list vide)
 - Les ingrédients créés précédemment contenus dans une list.

Créez une classe Poele avec une list comme contenu.

 Ajoutez une méthode cuire() qui, après 4 secondes, met l'état 'cuit' à self.contenu[0]. 
 Vous pouvez utiliser la fonction time.sleep(4).

Créez une classe Bol avec une list comme contenu.
 Ajoutez une méthode melanger(nom_melange) qui va créer un nouvel objet "new_melange"
 avec comme nom la variable nom_melange passée en paramètre et avec 'pas cuit' en état.
 Cette méthode remplacera self.contenu par [l'objet new_melange].

Début de la préparation de l'omelette :
 Pour indiquer que le personnage est à la maison :
 Utilisez la méthode se_deplacer avec l'objet Maison en paramètre.
 Affichez un message tel que : print(personnage.nom + " est actuellement à la " + personnage.lieu)

 Pour aller à l'épicerie acheter les ingrédients pour l'omelette :
 Répétez la première étape en changeant le paramètre de la méthode se_deplacer par l'épicerie.
 Le personnage prend un des paniers dans l'épicerie (récupère le panier dans les objets de l'épicerie et le met dans sa main droite).
 Affichez un message du type : print(f"{personnage.nom} a pris un panier")

Créez une boucle qui prend chaque élément (ingrédient) du contenu de l'épicerie (1 à 1) et en fait une COPIE dans le panier du personnage.
 Affichez un message à chaque ingrédient pris.
 Payez chaque ingrédient récupéré dans le panier avec la fonction payer_article().
 Affichez un message sur l'argent restant sur le personnage.

 Retournez à la maison (pour pouvoir cuisiner) :
 Utilisez la méthode se_deplacer avec l'objet Maison en paramètre.
 Affichez un message.

 Mettez chaque ingrédient dans le bol (1 à 1 avec une boucle) :
 Vérifiez que les ingrédients ne se trouvent plus dans le panier.
 Affichez un message pour chaque ingrédient mis dans le bol.

 Retournez à l'épicerie pour rapporter le panier :
 Utilisez la méthode se_deplacer avec l'objet Épicerie en paramètre.
 Enlevez le panier de la main droite du personnage et remettez-le dans les paniers de l'épicerie.
 Affichez un message.

 Retournez à la maison pour continuer l'omelette :
 Utilisez la méthode se_deplacer avec l'objet Maison en paramètre.
 Affichez un message.
 Vérifiez chaque ingrédient dans le bol et le coupez seulement s'il est entier avec la méthode couper de la personne.

 Mélangez le contenu du bol avec la méthode melanger. Nommez ce mélange une 'omelette' (à passer en paramètre).
 Affichez un message avec le nouveau mélange.
 Videz le contenu du bol dans la poêle. Il ne doit plus rien avoir dans le bol et il doit y avoir juste l'omelette pas cuite.

 Cuisez l'omelette avec la méthode de la poêle.
 Affichez un message final : print("Notre omelette est cuite :)")
 '''
#import
import time 


class Panier():
    instances = []

    def __init__(self,type="Panier",contenu=None):
        self.type = type 
        self.contenu = [] if contenu is None else contenu
        Panier.instances.append(self)

class Personnage():
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


class Lieu():
    def __init__(self, nom, personnes = None):
        self.nom = nom
        self.personnes = [] if personnes is None else personnes


class Outil():
    def __init__(self,nom,action):
        self.nom = nom
        self.action = action
        
class Ingredient():
    instances = []

    def __init__(self, nom, prix:float, etat = "Entier"):
        self.nom = nom
        self.prix = prix
        self.etat = etat 
        Ingredient.instances.append(self)

    def __str__(self):
        return self.nom
    
    def __repr__(self):
        return self.nom

class Shop(Lieu):
    def __init__(self,nom, personnes=None, paniers=None,ingredients=None):
        super().__init__(nom,personnes=None)
        self.paniers = [] if paniers is None else paniers
        self.ingredients = [] if ingredients is None else ingredients

class Bol():
    def __init__(self,contenu=None):
        self.contenu = [] if contenu is None else contenu

    def battre(self,nom_melange):
        new_ingr = Ingredient(nom_melange,0,"cru")
        self.contenu = nom_melange
        return new_ingr

class Poelle():
    def __init__(self, contenu = None):
        self.contenu = [] if contenu is None else contenu
    
    def cuire(self,ingredient):
        time.sleep(1)
        print("Cuisson en cours...")
        time.sleep(3)
        ingredient.etat = "cuit"
        print(f"Notre {ingredient.nom} est cuite")
    
    
#instanciation des objects utilisés dans le prog

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

def main():
    print(f"Ou est David: {david.lieu}")
    david.seDeplacer(maison)
    print(f"Ou est David: {david.lieu}")

    david.seDeplacer(epicerie)
   
    print(f"panier du shop contient : {panier_1.contenu}")
    print(f"Les main de Dav : {david.main_gauche}")

    david.attraper(panier_1)
    print(f"Les main de Dav : {david.main_gauche}")

    print(f"Avant de passer à la caisse {david.nom} a {david.argent} en poche")

    for i in david.main_gauche :
        print(i)
        david.payerArticle(i)

    print(f"Après être passer à la caisse {david.nom} a {david.argent} en poche")

    david.seDeplacer(maison)

    print(david.lieu)

    for i in david.main_gauche:
        mon_bol.contenu.append(i)
    david.main_gauche = []
    
    print(f"Dans mon bol y a : {mon_bol.contenu}")
    print(david.main_gauche)

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
    #je vide mon bol 
    mon_bol.contenu = []
    print(f"Dans ma poelle now j'ai : {ma_poelle.contenu}")
    
    print(omelette.etat)
    ma_poelle.cuire(omelette)
    #vérif etat 
    print(omelette.etat)


main()



