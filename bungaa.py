from turtle import *

color("purple")
title("art")
speed(-5)
r,g,b=200,0,0
def fleur():
    for i in range (300):
        begin_fill()
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(18)
        end_fill
        
fleur()
mainloop()