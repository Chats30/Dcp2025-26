import py5

def setup():
    py5.size(400, 400)
    py5.background(255, 0, 0)  # Set the background to red

def draw():
    py5.background(255, 0, 0)  # Keep the background red each frame as a safeguard
    py5.fill(255, 255, 0)  # Yellow color for the circle
    py5.ellipse(200, 200, 320, 320)  # Draw the yellow circle

    py5.fill(173, 216, 230)  # Light blue color for the triangle
    py5.triangle(200, 120, 120, 280, 280, 280)  # Draw the light blue triangle

    py5.fill(255, 255, 255)  # White color for the eyeball
    py5.ellipse(200, 250, 40, 40)  # Draw the eyeball

    py5.fill(0, 0, 0)  # Black color for the pupil
    py5.ellipse(200, 250, 16, 16)  # Draw the pupil

def key_pressed():
    if py5.key == py5.ESC:
        py5.exit_sketch()

py5.run_sketch()
