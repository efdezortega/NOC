increment = 0.01

def setup():    
    size(900, 900)
    noLoop()
    
def draw():
    loadPixels()
    xoff = 0.0
    for x in range(width):    
        xoff += increment
        yoff = 0.0    
        for y in range(height):        
            yoff += increment
            bright = noise(xoff, yoff) * 255
            pixels[x + (y * width)] = color(bright)
    updatePixels()
