
#  Pour utiliser la librairie pygame et avoir le son il faut l'installer avec la commande suivante :
#  pip install pygame et le fichier wav doit être dans le meme folder que le fichier code ;-)
#  Idem pour le graphisme il faut installer Pillow (pip install pillow)

#import libraries nécessaires

import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from PIL import Image, ImageTk
import time
import threading
import pygame 
import sys
import io
import queue


#definition de mes classes 

class Panier():
# Panier: Représente un panier avec un type (par défaut "Panier") et un contenu (une liste d'objets, par défaut vide)
    def __init__(self,type="Panier",contenu=None):
        self.type = type 
        self.contenu = [] if contenu is None else contenu
    
    def MontrerContenu(self):
        print(f"Le panier contient : {self.contenu}")
        
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
        if self.nom not in destination.personnes:
            destination.personnes.append(self.nom)
        print(f"{self.nom} se déplace...")
        time.sleep(1.5)
        print(f"{self.nom} est arrivé à {destination.nom}")
    
    def payerArticle(self, article):
        self.argent -= article.prix
        print(f"{self.nom} paie {article.nom} au prix de {article.prix}")
    
    def couper(self, ingredient, outil):
        ingredient.etat = "coupé"
        print(f"Je découpe {ingredient.nom} avec {outil.nom}!")
    
    def attraper(self,panier):
        for i in panier.contenu: 
            self.main_gauche.append(i)
        
        print(f"{self.nom} a attrapé l'article : {panier.contenu}")
        panier.contenu = []
    
    def rendrePanier(self):
        print(f"- Voici votre panier de retour Mr l'épicier.")
        print(f"- Merci {self.nom}. A bientôt!!!")

    def localiser(self):
        print(f"{self.nom} se trouve à : {self.lieu}")

    def detientQuoiEnMain(self):
        print(f"{self.nom} a en main les articles suivants \n: {self.main_gauche}")

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
        print(f"Je bas {nom_melange}")
        return new_ingr
    
    def nettoyer(self):
        self.contenu = []
        print("Je vide et noettoie le bol!")
        time.sleep(3)
        print("Ton bol est désormais vide et nettoyé!")
    
    def transvaserDans(self,recipient):
        recipient.contenu = self.contenu
        print(f"Tout est transvaser dans la poelle!")
    
    def contientQuoi(self):
        print(f"Dans mon bol j'ai : {self.contenu}")

class Poelle():
# Poelle: Représente une poêle avec un contenu (une liste d'objets, par défaut vide).
    def __init__(self, contenu = None):
        self.contenu = [] if contenu is None else contenu
        pygame.mixer.init()  # Initialize the mixer
        pygame.mixer.music.load("pan_noise.wav") 
        

    def cuire(self,ingredient):
        print(f"Cuisson de notre {ingredient.nom} en cours...")
        pygame.mixer.music.play()
        app.animer_PersoAnime()
        time.sleep(5)
        pygame.mixer.music.stop()
        ingredient.etat = "cuit"
        print(f"Notre {ingredient.nom} est cuite")

    def contientQuoi(self):
        print(f"Dans ma poelle now j'ai : {self.contenu}")
    
class TkinterRedirector(io.TextIOBase):
    def __init__(self, widget):
        self.widget = widget
        self.queue = queue.Queue()

    def write(self, string):
        self.queue.put(string)
        self.widget.after_idle(self.process_queue)
        return len(string)

    def flush(self):
        pass

    def process_queue(self):
        while not self.queue.empty():
            self.widget.insert(tk.END, self.queue.get())
            self.widget.see(tk.END)  # Fait défiler vers le bas pour montrer le texte ajouté

class PersoAnime:
    def __init__(self, canvas, x, y, largeur_corps, hauteur_corps, rayon_tete, hauteur_jambes):
        self.canvas = canvas

        # Corps (rectangle)
        self.corps = canvas.create_rectangle(x - largeur_corps/2, y - hauteur_corps/2,
                                             x + largeur_corps/2, y + hauteur_corps/2, fill="blue")

        # Tête (cercle)
        self.tete = canvas.create_oval(x - rayon_tete, y - hauteur_corps/2 - rayon_tete,
                                        x + rayon_tete, y - hauteur_corps/2, fill="red")

        # Bras gauche
        self.bras_gauche = canvas.create_line(x - largeur_corps/2, y - hauteur_corps/4,
                                              x - largeur_corps/2 - 20, y - hauteur_corps/4 - 20, width=5, fill="brown")

        # Main gauche
        self.main_gauche = canvas.create_oval(x - largeur_corps/2 - 25, y - hauteur_corps/4 - 25,
                                              x - largeur_corps/2 + 5, y - hauteur_corps/4 + 5, fill="pink")

        # Bras droit
        self.bras_droit = canvas.create_line(x + largeur_corps/2, y - hauteur_corps/4,
                                             x + largeur_corps/2 + 20, y - hauteur_corps/4 - 20, width=5, fill="brown")

        # Main droite
        self.main_droite = canvas.create_oval(x + largeur_corps/2 - 5, y - hauteur_corps/4 - 25,
                                              x + largeur_corps/2 + 25, y - hauteur_corps/4 + 5, fill="pink")

        # Jambes (deux rectangles)
        self.jambe_gauche = canvas.create_rectangle(x - largeur_corps/4, y + hauteur_corps/2,
                                                    x, y + hauteur_corps/2 + hauteur_jambes, fill="green")

        self.jambe_droite = canvas.create_rectangle(x, y + hauteur_corps/2,
                                                     x + largeur_corps/4, y + hauteur_corps/2 + hauteur_jambes, fill="green")

        # Poêle (cercle avec un rectangle comme manche)
        self.poele = canvas.create_oval(x + 20, y - 50, x + 120, y - 20, fill="gray")

       

    def seDeplacer(self, dx, dy):
        self.canvas.move(self.corps, dx, dy)
        self.canvas.move(self.tete, dx, dy)
        self.canvas.move(self.bras_gauche, dx, dy)
        self.canvas.move(self.main_gauche, dx, dy)
        self.canvas.move(self.bras_droit, dx, dy)
        self.canvas.move(self.main_droite, dx, dy)
        self.canvas.move(self.jambe_gauche, dx, dy)
        self.canvas.move(self.jambe_droite, dx, dy)
        self.canvas.move(self.poele, dx, dy)

    def remuerPoelle(self):
        for _ in range(3):
            self.canvas.move(self.poele, 10, 0)
            self.canvas.update()
            time.sleep(0.5)
            self.canvas.move(self.poele, -10, 0)
            self.canvas.update()
            time.sleep(0.5)

    def cuireOmelette(self):
        for _ in range(3):
            self.canvas.itemconfig(self.poele, fill="orange")
            self.canvas.update()
            time.sleep(0.5)
            self.canvas.itemconfig(self.poele, fill="gray")
            self.canvas.update()
            time.sleep(0.5)
        self.canvas.itemconfig(self.poele, fill="orange")
        self.canvas.update()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cooking Simulator")
        self.create_widgets()

        self.canvas = tk.Canvas(self, width=400, height=210, bg="dark blue")
        self.canvas.pack()

        largeur_corps = 40
        hauteur_corps = 80
        rayon_tete = 30
        hauteur_jambes = 43

        self.persoAnime = PersoAnime(self.canvas, 100, 100, largeur_corps, hauteur_corps, rayon_tete, hauteur_jambes)

        # Redirige sys.stdout vers le widget Text
        sys.stdout = TkinterRedirector(self.text_widget)

    def animer_PersoAnime(self):
        self.persoAnime.seDeplacer(100, 0)
        self.persoAnime.remuerPoelle()
        self.persoAnime.cuireOmelette()

    def create_widgets(self):
        self.label = tk.Label(self, text="Bienvenue dans le \n Cooking Simulator de David!", font=("Courier", 16))
        self.label.pack(pady=20)

        self.text_widget = scrolledtext.ScrolledText(self, height=10, width=50)
        self.text_widget.pack(pady=10)

        self.start_button = tk.Button(self, text="Démarrer", command=self.start_simulation)
        self.start_button.pack(pady=10)

        self.quit_button = tk.Button(self, text="Quitter", command=self.destroy)
        self.quit_button.pack(pady=10)
    
    def start_simulation(self):
        # Insérez ici le code de simulation (éventuellement l'appel à votre fonction main())
        print("C'est parti!!!")
        thread = threading.Thread(target=main)
        thread.start()

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


# Ensuite, il simule une série d'actions de David, telles que se déplacer, attraper un panier, 
# payer des articles, retourner à la maison, couper des ingrédients, battre des ingrédients dans un bol, 
# et enfin cuire dans une poêle

def main():
# La fonction main() appelle ces actions pour simuler le déroulement du scénario.
# Le résultat final est la création d'une omelette dans la poêle à partir des ingrédients dans le bol.
    time.sleep(2)
    print(f"Je check où se trouve David \nen utilisant ma fonction localiser")
    david.localiser()
    david.seDeplacer(maison)  
    print(f"Je check où se trouve David après déplacement")  
    david.localiser()

    time.sleep(2)
    david.seDeplacer(epicerie)
    time.sleep(4)
    

    panier_1.MontrerContenu()
    time.sleep(2)
    david.detientQuoiEnMain()
    time.sleep(2)
    david.attraper(panier_1)
    time.sleep(3)
    david.detientQuoiEnMain()
    time.sleep(4)
    print("Avant de payer ses articles à l'épicerie,")
    david.avoirEnPoche()
    time.sleep(2)
    for i in david.main_gauche :
        david.payerArticle(i)
        time.sleep(0.5)
    time.sleep(3)
    print("Après avoir payer,")
    
    david.avoirEnPoche() 
    time.sleep(4)
    
    david.seDeplacer(maison)
    time.sleep(4)

    print("Je mets les ingredients dans le bol pour melanger tout ça!")
    for i in david.main_gauche:
        mon_bol.contenu.append(i)
    david.main_gauche = []
    time.sleep(3)
    mon_bol.contientQuoi()
    time.sleep(3)
    david.detientQuoiEnMain()
    time.sleep(2)
    
    david.seDeplacer(epicerie)
    time.sleep(2)
    david.rendrePanier()
    david.seDeplacer(maison)
    time.sleep(4)
    
    for i in mon_bol.contenu:
        if i.etat == "Entier":
            david.couper(i, mon_couteau)
            time.sleep(2)

    omelette = mon_bol.battre("omelette")
    time.sleep(3)
    mon_bol.contientQuoi()
    time.sleep(2)
    mon_bol.transvaserDans(ma_poelle)
    time.sleep(3)
    mon_bol.nettoyer()
    time.sleep(2)
    ma_poelle.contientQuoi()
    time.sleep(3)
    ma_poelle.cuire(omelette)


if __name__ == "__main__":
    app = Application()
    app.mainloop()




