import pygame  # Bibliothèque pour l'affichage graphique
import sys     # Pour quitter le programme

#  Constantes 
LIGNES: int = 6      # Nombre de lignes de la grille
COLONNES: int = 7   # Nombre de colonnes de la grille
TAILLE_CASE: int = 80  # Taille d'une case en pixels
RAYON: int = TAILLE_CASE // 2 - 5  # Rayon du jeton
LARGEUR: int = COLONNES * TAILLE_CASE  # Largeur de la fenêtre
HAUTEUR: int = (LIGNES + 1) * TAILLE_CASE  # Hauteur de la fenêtre (+1 pour la zone du joueur)
TAILLE_FENETRE: tuple[int, int] = (LARGEUR, HAUTEUR)

# Couleurs utilisées
BLEU: tuple[int, int, int] = (0, 0, 255)
NOIR: tuple[int, int, int] = (0, 0, 0)
ROUGE: tuple[int, int, int] = (255, 0, 0)
JAUNE: tuple[int, int, int] = (255, 255, 0)

# Fonctions 
def creer_grille() -> list[list[str]]:
    grille = []
    for numero_ligne in range(LIGNES):
        ligne = []
        for numero_colonne in range(COLONNES):
            ligne.append(" ")
        grille.append(ligne)
    return grille
   

def jouer_coup(grille: list[list[str]], colonne: int, pion: str) -> int | None:
    for i in range(LIGNES-1, -1, -1):
        if grille[i][colonne] == " ":
            grille[i][colonne] = pion
            return i  # retourne la ligne où le pion a été placé
    return None  # colonne pleine


def verifier_victoire(grille: list[list[str]], pion: str) -> bool:
    # Horizontal
    for i in range(LIGNES):
        for j in range(COLONNES-3):
            if all(grille[i][j+k] == pion for k in range(4)):
                return True
    # Vertical
    for i in range(LIGNES-3):
        for j in range(COLONNES):
            if all(grille[i+k][j] == pion for k in range(4)):
                return True
    # Diagonale /
    for i in range(3, LIGNES):
        for j in range(COLONNES-3):
            if all(grille[i-k][j+k] == pion for k in range(4)):
                return True
    # Diagonale \
    for i in range(LIGNES-3):
        for j in range(COLONNES-3):
            if all(grille[i+k][j+k] == pion for k in range(4)):
                return True
    return False


def dessiner_grille(grille: list[list[str]], screen: pygame.Surface) -> None:
    for c in range(COLONNES):
        for r in range(LIGNES):
            pygame.draw.rect(screen, BLEU, (c*TAILLE_CASE, (r+1)*TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))
            couleur = NOIR
            if grille[r][c] == "Rouge":
                couleur = ROUGE
            elif grille[r][c] == "Jaune":
                couleur = JAUNE
            pygame.draw.circle(screen, couleur, (c*TAILLE_CASE + TAILLE_CASE//2, (r+1)*TAILLE_CASE + TAILLE_CASE//2), RAYON)
    pygame.display.update()


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode(TAILLE_FENETRE)
    pygame.display.set_caption("Puissance 4")
    font = pygame.font.SysFont("monospace", 20)

    grille = creer_grille()
    game_over = False
    joueur = "Rouge"

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                # Affiche le pion au dessus pour voir où il tombera
                screen.fill(NOIR, rect=(0, 0, LARGEUR, TAILLE_CASE))
                posx = event.pos[0]
                couleur = ROUGE if joueur == "Rouge" else JAUNE
                pygame.draw.circle(screen, couleur, (posx, TAILLE_CASE // 2), RAYON)
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                colonne = event.pos[0] // TAILLE_CASE
                ligne = jouer_coup(grille, colonne, joueur)
                if ligne is not None:
                    dessiner_grille(grille, screen)
                    if verifier_victoire(grille, joueur):
                        screen.fill(NOIR)
                        text = font.render(f"Joueur {joueur} gagne!", True, ROUGE if joueur == "Rouge" else JAUNE)
                        screen.blit(text, (10, HAUTEUR // 2 - 10))
                        pygame.display.update()
                        pygame.time.wait(5000)
                        game_over = True
                    joueur = "Jaune" if joueur == "Rouge" else "Rouge"
        dessiner_grille(grille, screen)

    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()
