import turtle as trt
slow_guy = trt.Turtle()
scr = trt.Screen()
scr.listen()
def move_forward():
    slow_guy.forward(10)
def move_backward():
    slow_guy.backward(10)
def turn_right():
    slow_guy.right(10)
def turn_left():
    slow_guy.left(10)
def clear():
    slow_guy.reset()
    
    
    
trt.onkey(fun = move_forward, key = "w")
trt.onkey(fun = move_backward, key = "s")
trt.onkey(fun = turn_right, key = "d")
trt.onkey(fun = turn_left, key = "a")
trt.onkey(fun = clear, key ="c")
trt.ondrag(trt.goto)







scr.title("Etch-and-Sketch Game")   
scr.exitonclick()