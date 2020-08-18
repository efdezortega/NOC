class Walker(object):

    def __init__(self):
        self.x = width / 2
        self.y = height / 2
        self.t_x = 0
        self.t_y = 10000

    def display(self):
        noStroke()
        fill(255, 50)
        rectMode(CENTER)
        rect(self.x, self.y, 2, 2)

    # Randomly move up, down, left, right, or stay in one place
    def walk(self):
        
        n_x = noise(self.t_x)
        n_y = noise(self.t_y)
          
        self.t_x += 0.005   
        self.t_y += 0.005
                                        
        vx = map(n_x, 0, 1, -2, 2)
        vy = map(n_y, 0, 1, -2, 2)
        
        self.x += vx
        self.y += vy
        # Stay on the screen
        self.x = self.x % width
        self.y = self.y % height

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
