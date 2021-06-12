#Este programa que desenha sete cículos um na frente do outro
#seguindo a sequência de cores do arco-íris 


import turtle

amanda = turtle.Turtle()
#definir a cor da janela de comando
amanda.screen.bgcolor("black")
print(amanda)

#comando para preencher os círculos
amanda.fillcolor()

#Função circle define cada circulo em uma posicão e de cor diferente
def circle(circle,position,heading):
    amanda.begin_fill()
    amanda.color("red")
    amanda.forward(-150)
    amanda.circle(120)
    amanda.position()
    (0.00,0.00)
    amanda.heading()
    0.0
    amanda.end_fill()

    amanda.begin_fill()
    amanda.color("orange")
    amanda.forward(40)
    amanda.circle(100)  
    amanda.position()
    (0.00,0.00)
    amanda.heading()
    0.0
    amanda.end_fill()

    amanda.begin_fill()
    amanda.color("yellow")
    amanda.forward(60)
    amanda.circle(80)  
    amanda.position()
    (0.00,0.00)
    amanda.heading()
    0.0
    amanda.end_fill()

    amanda.begin_fill()
    amanda.color("green")
    amanda.forward(80)
    amanda.circle(60)  
    amanda.position()
    (0.00,0.00)
    amanda.heading()
    0.0
    amanda.end_fill()

    amanda.begin_fill()
    amanda.color("light blue")
    amanda.forward(60)
    amanda.circle(40)  
    amanda.position()
    (0.00,0.00)
    amanda.heading()
    0.0
    amanda.end_fill()

    amanda.begin_fill()
    amanda.color("dark blue")
    amanda.forward(40)
    amanda.circle(20)  
    amanda.position()
    (0.00,0.00)
    amanda.heading()
    0.0
    amanda.end_fill()

    amanda.begin_fill()
    amanda.color("purple")
    amanda.forward(20)
    amanda.circle(10)  
    amanda.position()
    (0.00,0.00)
    amanda.heading()
    0.0
    amanda.end_fill()

circle(amanda,100,0)

#Função write onde consigo escrever na janela de comando do turtle
def write(write):
    amanda.color("white")
    amanda.write("FIM!!!",move=True, align="right",font=("Verdana", 100, "normal"))
    
write(amanda)