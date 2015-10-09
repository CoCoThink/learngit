import turtle
def drawSnake( rad,angle,len,neckrad):
    for i in range(len):
    #画圆弧（半径，角度）
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    #画直线
    turtle.fd(rad*2/3)
        
def main():
#初始化窗口（宽度，高度，距屏幕左边距离，距屏幕顶边距离）
    turtle.setup(1300,700,0,20)
    pythonsize=30
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    #定义初始爬行方向
    turtle.seth(-40)
    drawSnake(40,80,5,pythonsize/2)

main()

