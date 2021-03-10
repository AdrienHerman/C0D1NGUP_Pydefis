from turtle import *

# Il commence à l'est
color("red")
degrees()

chaine = "NNEESOOESEENNEEOOSEOSEEENNESENSSENNEESSOOEEENNEEOOSEOSEEENEENOOEESOOSEEEEEEENONSESENNSSENNEESSOOEEENNSSEENNSSEEENOONEEOOSEESEEEENNEESSOOEEENNEESOOEESENNESENSSEEENOONEEOOSEESEEEENNSSEEENNEESOOEESEEEENNEEOOSEOSEEENNEESSOOEEENNEESOOESEENNEEOOSEOSEEEENNOEEOSSEEEEENNEESOOEESOOEEENNEESOOESEENNSSEENNSSENNESNESSENNEEOOSEOSEEENNSSEENNSSEEENOONEEOOSEESENNEEOOSEOSEEEEEENNEESSOOEEENNEEOOSEOSEEENNESNESSENNEESOOEESENNSSENNESENSS"
"""
270 : Nord
0 : Est
90 : Sud
180 : Ouest
"""

for c in chaine:
    if c == "N":
        angle = 270 + heading()
        right(angle)
        pendown()
    elif c == "S":
        angle = 90 + heading()
        right(angle)
        pendown()
    elif c == "E":
        angle = heading()
        right(angle)
        pendown()
    elif c == "O":
        angle = 180 + heading()
        right(angle)
        pendown()
    
    forward(10)
    penup()

a = input()
