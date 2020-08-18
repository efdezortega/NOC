class Walker(object):

    def __init__(self):
        self.x = width / 2
        self.y = height / 2

    def display(self):
        noStroke()
        fill(255, 75)
        rectMode(CENTER)
        rect(self.x, self.y, 2, 2)

    # Randomly move up, down, left, right, or stay in one place
    def walk(self):
        
        g_x = randomGaussian()
        g_y = randomGaussian()
        sd = 2
        
        vx = g_x * sd
        vy = g_y * sd
        self.x += vx
        self.y += vy
        # Stay on the screen
        self.x = constrain(self.x, 0, width - 1)
        self.y = constrain(self.y, 0, height - 1)

def setup():
    size(900, 900)
    frameRate(300)
    background(0)
    # Create a walker object
    global w
    w = Walker()

def draw():
    # background(255)
    # Run the walker object
    w.walk()
    w.display()
