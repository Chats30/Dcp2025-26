import py5


mode = 0
last_pressed = False
circle_size = 50

def setup():
    py5.size(800, 600)
    py5.rect_mode(py5.CENTER)
    py5.ellipse_mode(py5.CENTER)

def draw_face():
    x,y = py5.mouse_x, py5.mouse_y
    py5.fill(255, 255, 0)
    py5.ellipse(x,y, 100, 100)
    py5.ellipse(x - 20, y - 10, 15, 20)
    py5.ellipse(x + 20, y - 10, 15, 20)
    
    py5.no_fill()
    py5.stroke(0)
    py5.arc(x, y + 10, 40, 30, 0, py5.PI) # Used arc for the mouth

def mouse_pressed():
    global circle_size
    circle_size += 10 # To increase Circle size when clicked 

def draw_circle():
    py5.background(0)
    py5.circle(py5.width/2, py5.height/2, circle_size)
    py5.fill(255, 0, 0) 
    

    

def draw():
    global mode, last_pressed
    py5.background(0,255, 255)

    if mode == 0:
        draw_face()
    if mode == 1:
        draw_circle()

    if py5.is_key_pressed: # I am having issues when changing modes while running, you have to click 1 twice to get into mode 1  
        if not last_pressed:
            mode = (mode + 1) % 4
            last_pressed = True
        else:
            last_pressed = False

    
py5.run_sketch()
