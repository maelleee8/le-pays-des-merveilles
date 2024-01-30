import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur_fenetre = 400
hauteur_fenetre = 400

# Couleurs
blanc = (255, 255, 255)

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jet de dé")

# Initialisation du résultat du dé avec un nombre aléatoire entre 1 et 6
resultat_initial = random.randint(1, 6)
resultat_de = resultat_initial

# Chargement des images des faces du dé
images_faces_de = [
    pygame.image.load("dk bas.png"),
    pygame.image.load("dk droit.png"),
    pygame.image.load("dk gauche.png"),
    pygame.image.load("dk haut.png"),
    pygame.image.load("dk haut.png"),
    pygame.image.load("dk gauche.png"),
]

# Font pour le texte
font = pygame.font.Font(None, 36)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Détection de l'appui sur une touche
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Jet de dé
            resultat_de = random.randint(1, 6)
            print("Résultat du dé :", resultat_de)

    # Effacer l'écran
    fenetre.fill(blanc)

    # Afficher l'image du dé
    fenetre.blit(images_faces_de[resultat_de - 1], (50, 50))

    # Afficher les résultats du dé et du nombre initial sous forme de texte à côté de l'image
    texte_initial = font.render(str(resultat_initial), True, (0, 0, 0))
    texte_de = font.render(str(resultat_de), True, (0, 0, 0))
    
    fenetre.blit(texte_initial, (120, 50))
    fenetre.blit(texte_de, (120, 90))

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()