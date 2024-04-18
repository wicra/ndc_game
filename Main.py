import pyxel
from random import randint
# Initialisation des variables globales
global direction
global score

direction=[1,0]
score=0

#constante du jeu
TITLE="Serpen_venimeux"
WIDTH=200
HEIGHT=160
CASE=20
FRAME_REFRESH = 15
snake= [[3, 3],[2, 3],[1, 3]]
food = [8,3]



#création de fenetre
pyxel.init(WIDTH,HEIGHT,title=TITLE)




def draw():
    #Ecran effacer et replir  en noir par la valeur (0)
    pyxel.cls(0)

    #dessiner le corps en vert (11)
    for anneau in snake[1:]:
        x, y = anneau[0], anneau[1]
        pyxel.rect(x * CASE, y * CASE, CASE, CASE,11)

    #tete en orange (9)
    x_head, y_head = snake[0]
    pyxel.rect(x_head * CASE, y_head * CASE,CASE, CASE ,9)

    #Le scor en blanc (7)
    pyxel.text(4, 4, f"SCORE :{score}",7)


def update():
    # Utilisation des variables globales
    global direction , score #pour déclarer qu'on peut changer

    #FPS
    if pyxel.frame_count % FRAME_REFRESH==0:
        #deplacement ver direction
        head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

        #on l'insert au début
        snake.insert(0,head)
        #On supprime le dernier case pour montrer le deplacement
        snake.pop(-1)

    #on suit les instruction du jouer

    
    if pyxel.btn(pyxel.KEY_ESCAPE):
        exit()
    elif pyxel.btn(pyxel.KEY_RIGHT) and direction in ([0 ,1], [0 ,-1]):
        direction = [1,0]
    elif pyxel.btn(pyxel.KEY_LEFT) and direction in ([0 ,1], [0 ,-1]):
        direction = [-1, 0]

    if head in snake[1:] \
            or head [0] < 0 \
            or head[0] > WIDTH/CASE - 1 \
            or head[1]<0\
            or head[1]> HEIGHT/CASE - 1:
        pyxel.quit()

    x_food, y_food = food
    pyxel.rect(x_food * CASE, y_food * CASE,CASE,CASE,8)

    while food in snake:
        food=[randint(0,WIDTH/CASE -1),randint(0,HEIGHT/CASE - 1)]

pyxel.run(update,draw)
