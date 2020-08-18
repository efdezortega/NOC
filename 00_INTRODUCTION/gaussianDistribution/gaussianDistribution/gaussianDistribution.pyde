def setup():
    size(900,450)
    background(0)

def draw():
      
    g = randomGaussian()
    sd = 60
    mean = width /2
    
    x = (sd * g) + mean
    
    fill(255, 10)
    noStroke()
    ellipse(x, height / 2, 15, 15)
