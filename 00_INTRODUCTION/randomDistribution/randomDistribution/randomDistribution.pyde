randomCounts =[0.0] * 20

def setup():
    size(500, 250)
    
def draw():
    background(245)
    
    index = int(random(len(randomCounts)))    
    randomCounts[index] += 1
    
    stroke(100)
    strokeWeight(1)
    fill(200)
    
    textSize(10)
    
    w = width / len(randomCounts)
    
    for x, r in enumerate(randomCounts):
        fill(200)
        rect(x * w, height - r, w , r)
        fill(100)
        text(str(int(r)), (x * w) + 1, (height - r) - 1)
    
    
    
