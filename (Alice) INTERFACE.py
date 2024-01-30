import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition de la taille de l'écran
largeur, hauteur = 800, 600
ecran_accueil = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Alice au Pays des Merveilles - Accueil")

# Définition des couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
gris = (169, 169, 169)

# Police pour le texte
police = pygame.font.Font(None, 36)

# Fonction pour afficher le texte
def afficher_texte(texte, x, y, couleur):
    texte_surface = police.render(texte, True, couleur)
    ecran_accueil.blit(texte_surface, (x, y))

# Fonction pour créer un bouton
def creer_bouton(x, y, largeur, hauteur, couleur, texte, action=None):
    rect = pygame.Rect(x, y, largeur, hauteur)
    pygame.draw.rect(ecran_accueil, couleur, rect)
    afficher_texte(texte, x + 10, y + 10, noir)

    clic_souris = pygame.mouse.get_pressed()
    if rect.collidepoint(pygame.mouse.get_pos()) and clic_souris[0] == 1 and action is not None:
        action()

# Fonction pour l'écran d'accueil
def ecran_accueil():
    ecran_accueil.fill(blanc)
    afficher_texte("Alice au Pays des Merveilles", 200, 50, noir)
    afficher_texte("Entrez les noms des joueurs (4 maximum):", 200, 200, noir)

    noms_joueurs = []
    input_boxes = [pygame.Rect(200, 250 + i * 60, 400, 50) for i in range(4)]
    couleur_active = pygame.Color('dodgerblue2')
    couleur_inactive = pygame.Color('lightskyblue3')
    couleurs = [couleur_inactive] * 4
    textes = [''] * 4
    actifs = [False] * 4

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, box in enumerate(input_boxes):
                    if box.collidepoint(event.pos):
                        actifs[i] = not actifs[i]
                    else:
                        actifs[i] = False
                    couleurs[i] = couleur_active if actifs[i] else couleur_inactive
            if event.type == pygame.KEYDOWN:
                for i, actif in enumerate(actifs):
                    if actif:
                        if event.key == pygame.K_RETURN:
                            noms_joueurs.append(textes[i])
                            textes[i] = ''
                        elif event.key == pygame.K_BACKSPACE:
                            textes[i] = textes[i][:-1]
                        else:
                            textes[i] += event.unicode

        ecran_accueil.fill(blanc)
        afficher_texte("Alice au Pays des Merveilles", 200, 50, noir)
        afficher_texte("Entrez les noms des joueurs (4 maximum):", 200, 200, noir)

        for i, box in enumerate(input_boxes):
            pygame.draw.rect(ecran_accueil, couleurs[i], box, 2)
            text_surface = police.render(textes[i], True, noir)
            width = max(200, text_surface.get_width() + 10)
            box.w = width
            ecran_accueil.blit(text_surface, (box.x + 5, box.y + 5))

        # Création du bouton Valider
        creer_bouton(200, 500, 150, 50, gris, "Valider", valider_action)

        pygame.display.flip()
        clock.tick(30)

        if len(noms_joueurs) == 4:
            break

    return noms_joueurs

# Fonction d'action pour le bouton Valider
def valider_action():
    print("Bouton Valider cliqué ! Passer à l'étape suivante...")
    lancer_interface_jeu()

# Fonction pour lancer l'interface du jeu
def lancer_interface_jeu():
    pygame.quit()
    sys.exit()

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 300 <= event.pos[0] <= 500 and 400 <= event.pos[1] <= 450:
                ecran_accueil()

    ecran_accueil.fill(blanc)
    afficher_texte("Alice au Pays des Merveilles", 200, 50, noir)
    creer_bouton(300, 400, 200, 50, gris, "Démarrer", lancer_interface_jeu)

    pygame.display.flip()