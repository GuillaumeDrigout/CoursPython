from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    print(pos())
    print(abs(pos()))
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
