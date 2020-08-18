def setup():
    size(900,900)
    background(0)
    frameRate(100)

def draw():
      
    g_x = randomGaussian()
    g_y = randomGaussian()    
    sd = 50
    mean = width /2
    
    x = (sd * g_x) + mean
    y = (sd * g_y) + mean
        
    fill(randomGaussian() * sd, randomGaussian() * sd, randomGaussian() * sd, 75)
    noStroke()
    
    ellipse(x, y, 10, 10)
