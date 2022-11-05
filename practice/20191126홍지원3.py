import turtle
t=turtle.Turtle()
t.shape("turtle")

#미로 그리는 함수
#위치좌표(x,y)

def draw_maze(x,y):
    for i in range(2):
        t.penup()
        if i ==1:
            t.goto(x+100,y+100)
        else:
            t.goto(x,y)
        t.pendown()
        t.forward(300)
        t.right(90)
        t.forward(300)
        t.left(90)
        t.forward(300)

#왼쪽, 오른쪽 방향키 함수
def turn_left():
    t.left(10)
    t.forward(10)

def turn_right():
    t.right(10)
    t.forward(10)

#그림 그리는 화면 얻기
screen=turtle.Screen()

#미로 그리기
#키보드 지정
draw_maze(-300,200)
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

#거북이 이동길
t.penup()
t.goto(-300,250)
t.speed(1)
t.pendown()

#프로그램이 잘 작동되도록 해주는 명령어
screen.listen()
screen.mainloop()
