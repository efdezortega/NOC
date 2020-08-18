class Walker(object):

    def __init__(self):
        self.x = width / 2
        self.y = height / 2

    def display(self):
        stroke(0)
        fill(50)
        rectMode(CENTER)
        rect(self.x, self.y, 2, 2)

    # Randomly move up, down, left, right, or stay in one place
    def walk(self):
        vx = random(-2, 2)
        vy = random(-2, 2)
        self.x += vx
        self.y += vy
        # Stay on the screen
        self.x = constrain(self.x, 0, width - 1)
        self.y = constrain(self.y, 0, height - 1)

def setup():
    size(500, 500)
    frameRate(100)
    background(245)
    # Create a walker object
    global w
    w = Walker()

def draw():
    # background(255)
    # Run the walker object
    w.walk()
    w.display()
    
def keyPressed():
    if key == 's' or key == 'S':
        pointIndex = str(os.path.basename(__file__)).index('.')
        save(str(os.path.basename(__file__))[:pointIndex])
        print('Saved Image')
