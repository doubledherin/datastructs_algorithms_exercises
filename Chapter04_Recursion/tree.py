from turtle import *

t = Turtle()
myWin = t.getscreen()

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-10, t)
        t.right(20)
        t.backward(branchLen)
    

t.left(90)
t.up()
t.backward(300)
t.down()
t.color('green')
tree(110, t)
myWin.exitonclick()
