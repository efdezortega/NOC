t = 0

def setup():
    size(900, 900)
    background(255)
    
def draw():
    global t
    n = noise(t)
    t += 0.01

    
