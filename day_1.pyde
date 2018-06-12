#Printing
print("hello world")

#Variables
    #Strings
greeting = "Hi there "
name = "Jeffersmith"
print(greeting + name)
     #Numbers
x = 5
y = 10
sum = x + y
print("the sum of %s and %s is %s" %(x, y, sum))

xpos = 0

def setup():
    size(1000, 1000)

def draw():
    #Colors and borders, and background
    background(155)
    fill(255) # fill with white
    stroke(0) #black border
    strokeWeight(5) #border thickness
    
    #rectangles
    rect(250, 350, 500, 300)
    
    #circles
    fill(200, 0, 0) #fill with red
    ellipse(500, 500, 300, 300)
    
    #triangles
    fill(0, 200, 0)
    triangle(250, 350, 750, 350, 500, 200)
    
    #lines
    stroke(255) #White line
    line(500, 650, 500, 1000)
    
    #text
    textSize(24)
    fill(255)
    text("Words go here", 420, 510)
    
    #Drawing using a variable
    global xpos
    fill(0, 0, 200)
    ellipse(xpos, 500, 100, 100)
    xpos = xpos + 1
    
def mousePressed():
    print("X: %s, Y: %s" %(mouseX, mouseY))
    
    #Conditionals
    global xpos
    distance = sqrt((mouseX - xpos)**2 + (mouseY - 500)**2)
    if distance < 50:
        print("You clicked the moving circle!")