# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import turtle

def escalier(tortue,iteration,longueur):
    tortue.forward(longueur)
    for i in range(0, iteration):

        tortue.left(90)
        tortue.forward(longueur)
        tortue.right(90)
        tortue.forward(longueur)

def carre(tortue,longueur):
    #tortue.forward(longueur)
    for i in range(0, 4):
        tortue.forward(longueur)
        tortue.left(90)

def carres(tortue,longueur,nbcarre):
    for i in range (1, nbcarre+1):
        carre(tortue, longueur)
        longueur += 10



# t = turtle.Turtle()
# t.speed(2)

t1 = turtle.Turtle()
t1.speed(10)

# escalier(t,5,30)

taille = 20

for i in range (0,4):
    carres(t1,taille,20)
    t1.left(90)

t1.forward(800)










turtle.done()