import math
from turtle import *

def hearta(x):
    return 15 * math.sin(x)**3

def heartb(x):
    return 12 * math.cos(x) - 5 * math.cos(2 * x) - 2 * math.cos(3 * x) - math.cos(4 * x)

speed(0)
bgcolor("pink")
penup() 
goto(0, 0)  
pendown() 
color("red")  


begin_fill() 
for i in range(6000):
    goto(hearta(i * 0.1) * 20, heartb(i * 0.1) * 20)  
    
end_fill()

penup()
goto(0,-30)
color ("red")
write("I love you", align="center", font=("Arial",24,"bold"))
done()  