from tkinter import *
import turtle as t



bd=120/2
lt=90/2
fd=(120/3)+10
select=['stone','paper','scissor']
class draw:
    
    def scissor():
        t.circle(20)
        t.right(90)
        t.forward(120)
        t.backward(bd)
        t.left(lt)
        t.forward(fd)
        t.right(180)
        t.forward(110)
        t.circle(20)

    def stone():
        t.fillcolor('gray')
        t.begin_fill()
        t.left(90)
        for s in range(93):
            t.speed(0)
            t.forward(5)
            t.left(2)
        t.left(85)
        t.forward(295)
        t.end_fill()
    def paper():
        for p in range(4):
            t.forward(150)
            t.left(90)
def title(name):
    t.title(str(name))
def clear():
    t.reset()        




 

