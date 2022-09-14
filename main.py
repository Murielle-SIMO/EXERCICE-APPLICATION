import turtle


#t.forward(100)
#t.left(90)
#t.forward(50)
#t.backward(100)
#t.right(45)
#t.forward(200)

def escalier (taille, nb):
    angle = 90

    for i in range(nb):
        t.forward(taille)
        t.left(angle)
        t.forward(taille)
        t.right(angle)
    t.forward(taille)
    # i += 1

def carre (taille):
    for i in range(4):
        t.forward(taille)
        t.left(90)

def carres (taille_depart, nb):
    taille = taille_depart
    for i in range(0, nb):
        taille = (i+1)*taille_depart
        carre(taille)


t = turtle.Turtle()

#carre (50)
#carre (100)
#escalier(50, 15)
carres(10, 5)

turtle.done()