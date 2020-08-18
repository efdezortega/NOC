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
                
        v = random(0.0, 1.0)
        #el *2 es por darle un poco de velocidad 
        if v < 0.25:
            if mouseX < self.x:
                self.x -= 2
            else:
                self.x += 2
                
            if mouseY < self.y:
                self.y -= 2
            else:
                self.y += 2
        else:
            vx = random(-2, 2)
            vy = random(-2, 2)
            self.x += vx
            self.y += vy

        # Stay on the screen
        self.x = constrain(self.x, 0, width - 1)
        self.y = constrain(self.y, 0, height - 1)

def setup():
    size(500, 500)
    frameRate(50)
    background(245)
    # Create a walker object
    global w
    w = Walker()

def draw():
    # background(255)
    # Run the walker object
    w.walk()
    w.display()
