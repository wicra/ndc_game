import pyxel

# États du jeu
STATE_MENU = 0
STATE_PLAYING = 1
STATE_PAUSED = 2

class Jeu:
    def __init__(self):
        # Taille de la fenêtre 128x128 pixels
        pyxel.init(128, 128, title="Nuit du c0de")

        # Position initiale des vaisseaux
        self.vaisseau1_x = 60
        self.vaisseau1_y = 10
        self.vaisseau2_x = 60
        self.vaisseau2_y = 120

        # État initial du jeu
        self.state = STATE_MENU

        pyxel.run(self.update, self.draw)

    def vaisseau_deplacement_1(self):
        """Déplacement du vaisseau 1 avec les touches de direction"""

        if pyxel.btn(pyxel.KEY_D) and self.vaisseau1_x < 120:
            self.vaisseau1_x += 1
        if pyxel.btn(pyxel.KEY_Q) and self.vaisseau1_x > 0:
            self.vaisseau1_x -= 1
        if pyxel.btn(pyxel.KEY_S) and self.vaisseau1_y < 120:
            self.vaisseau1_y += 1
        if pyxel.btn(pyxel.KEY_Z) and self.vaisseau1_y > 0:
            self.vaisseau1_y -= 1

    def vaisseau_deplacement_2(self):
        """Déplacement du vaisseau 2 avec les touches de direction"""

        if pyxel.btn(pyxel.KEY_RIGHT) and self.vaisseau2_x < 120:
            self.vaisseau2_x += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.vaisseau2_x > 0:
            self.vaisseau2_x -= 1
        if pyxel.btn(pyxel.KEY_DOWN) and self.vaisseau2_y < 120:
            self.vaisseau2_y += 1
        if pyxel.btn(pyxel.KEY_UP) and self.vaisseau2_y > 0:
            self.vaisseau2_y -= 1

    def update(self):
        """Mise à jour des variables (30 fois par seconde)"""

        if self.state == STATE_MENU:
            if pyxel.btnp(pyxel.KEY_1):
                self.state = STATE_PLAYING
            elif pyxel.btnp(pyxel.KEY_2):
                self.state = STATE_PAUSED
            elif pyxel.btnp(pyxel.KEY_3):
                pyxel.quit()
        elif self.state == STATE_PLAYING:
            # Déplacement des vaisseaux
            self.vaisseau_deplacement_1()
            self.vaisseau_deplacement_2()

    def draw(self):
        """Création et positionnement des objets (30 fois par seconde)"""

        # Vide la fenêtre
        pyxel.cls(0)

        if self.state == STATE_MENU:
            # Affichage du menu
            pyxel.text(50, 60, "Menu du jeu", 7)
            pyxel.text(40, 80, "1. Jouer", 7)
            pyxel.text(40, 90, "2. Pause", 7)
            pyxel.text(40, 100, "3. Quitter", 7)
        elif self.state == STATE_PLAYING:
            # Affichage des vaisseaux
            pyxel.rect(self.vaisseau1_x, self.vaisseau1_y, 8, 8, 12)
            pyxel.rect(self.vaisseau2_x, self.vaisseau2_y, 8, 8, 1)
        elif self.state == STATE_PAUSED:
            # Affichage de l'écran de pause
            pyxel.rect(40, 60, 48, 16, 1)
            pyxel.text(48, 68, "Pause", 7)

Jeu()

