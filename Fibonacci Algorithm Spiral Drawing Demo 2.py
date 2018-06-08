#Fibonacci Algorithm Spiral Drawing Demo 2
import turtle
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
 
prevNum = 0
currNum = 1
nextNum = prevNum + currNum 
fibNums = [prevNum, currNum ]
myTurtle.color('Red')
#Fibonacci Calculation
for i in range(14):
    nextNum = prevNum + currNum 
    prevNum = currNum 
    currNum = nextNum 
    fibNums.append(currNum )
 
#Draw a square
for x in fibNums:
    print(x)
    myTurtle.right(90)
    myTurtle.forward(x / 2)