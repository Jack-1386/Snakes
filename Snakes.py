import turtle
import time
import random

turtle.setup(600,600)

turtle.bgpic('bgpic.gif')

turtle.tracer(False)

turtle.addshape('egg.gif')
egg = turtle.Pen()
egg.shape('egg.gif')
egg.penup()
egg.goto(-180,-180)

turtle.addshape('head1.gif')
turtle.addshape('head2.gif')
turtle.addshape('head3.gif')
turtle.addshape('head4.gif')
turtle.addshape('body.gif')

snakeList = []

for i in range(5):
    t = turtle.Pen()
    if i == 0:
        t.shape('head1.gif')
    else:
        t.shape('body.gif')
    t.penup()
    t.goto(i*20,0)
    snakeList.append(t)

word = turtle.Pen()
word.penup()
word.goto(-225,265)
word.color('white')
word.write('5',font = ('微软雅黑',18))
word.hideturtle()

turtle.update()

def goLeft():
    x = snakeList[0].xcor()
    y = snakeList[0].ycor()
    t = snakeList.pop()
    t.hideturtle()
    t1 = turtle.Pen()
    t1.shape('head1.gif')
    snakeList.insert(0,t1) 
    t1.penup()
    t1.goto(x-20,y)
    snakeList[1].shape('body.gif')
    turtle.update()

def goRight():
    x = snakeList[0].xcor()
    y = snakeList[0].ycor()
    t = snakeList.pop()
    t.hideturtle()
    t1 = turtle.Pen()
    t1.shape('head3.gif')
    snakeList.insert(0,t1) 
    t1.penup()
    t1.goto(x+20,y)
    snakeList[1].shape('body.gif')
    turtle.update()

def goUp():
    x = snakeList[0].xcor()
    y = snakeList[0].ycor()
    t = snakeList.pop()
    t.hideturtle()
    t1 = turtle.Pen()
    t1.shape('head2.gif')
    snakeList.insert(0,t1) 
    t1.penup()
    t1.goto(x,y+20)
    snakeList[1].shape('body.gif')
    turtle.update()

def goDown():
    x = snakeList[0].xcor()
    y = snakeList[0].ycor()
    t = snakeList.pop()
    t.hideturtle()
    t1 = turtle.Pen()
    t1.shape('head4.gif')
    snakeList.insert(0,t1) 
    t1.penup()
    t1.goto(x,y-20)
    snakeList[1].shape('body.gif')
    turtle.update()

# ====================Test====================
'''
Test = 0  
while Test <= 5: 
    goLeft()
    time.sleep(0.5)
    Test += 1
'''
# ============================================

flag = 'left'

def up():
    global flag
    flag = 'up'

def left():
    global flag
    flag = 'left'

def down():
    global flag
    flag = 'down'

def right():
    global flag
    flag = 'right'

turtle.listen()

turtle.onkeypress(up,'w')
turtle.onkeypress(left,'a')
turtle.onkeypress(down,'s')
turtle.onkeypress(right,'d')

turtle.onkeypress(up,'W')
turtle.onkeypress(left,'A')
turtle.onkeypress(down,'S')
turtle.onkeypress(right,'D')

turtle.onkeypress(up,'Up')
turtle.onkeypress(left,'Left')
turtle.onkeypress(down,'Down')
turtle.onkeypress(right,'Right')


def eat():
    x_egg = egg.xcor()
    y_egg = egg.ycor()
    x_snHead = snakeList[0].xcor()
    y_snHead = snakeList[0].ycor()
    length = len(snakeList)
    if x_egg == x_snHead and y_egg == y_snHead:
        print('吃到了')
        x_egg = random.randint(-13,13)*20
        y_egg = random.randint(-13,13)*20
        egg.goto(x_egg,y_egg)
        t = turtle.Pen()
        t.shape('body.gif')
        snakeList.append(t)
        length += 1
        word.clear()
        word.write(length,font = ('微软雅黑',18))

while True:
    eat()
    if flag == 'up':
        goUp()
    elif flag == 'left':
        goLeft()
    elif flag == 'down':
        goDown()
    elif flag == 'right':
        goRight()
    time.sleep(0.2)
    if snakeList[0].xcor() == -300 or snakeList[0].ycor() == -300 or snakeList[0].xcor() == 300 or snakeList[0].ycor() == 300:
        score = '你得了',len(snakeList)-5,'分'
        word.penup()
        word.goto(-40,0)
        word.color('red')
        word.write('你死了',font = ('微软雅黑',24))
        word.goto(-85,-30)
        word.write('因为你碰到了边界',font = ('微软雅黑',18))
        word.goto(-80,-60)
        word.write(score,font = ('微软雅黑',18))
        break
    '''
    elif snakeList[0].xcor() == snakeList[-1].xcor() and snakeList[0].ycor() == snakeList[-1].ycor():
        word.penup()
        word.goto(-40,0)
        word.color('red')
        word.write('你死了',font = ('微软雅黑',24))
        word.goto(-90,-30)
        word.write('因为蛇头碰到了蛇尾',font = ('微软雅黑',18))
        break
  '''
print(score)
time.sleep(2)
turtle.bye()
