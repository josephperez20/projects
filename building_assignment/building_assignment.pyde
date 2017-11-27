def setup():
    size(200, 400)
    background(255, 250, 176)

def draw():
    fill(50)
    for i in range(10, height, 30):
        rect(15, i, 20, 20)
