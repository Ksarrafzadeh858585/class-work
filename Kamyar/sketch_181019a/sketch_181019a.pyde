 x = 0
 
 def setup():
    size(640,480)
    
 def draw():
     global x
    
     if x >= 640:
         x = 0
     x += 3
    
     background(135, 206, 250)
      
      
     noStroke()
     ellipse(x, 125, 50, 50)
     ellipse(x+30, 125, 50, 50)
     ellipse(x+10, 110, 50, 50)
     
     noStroke()
     fill(127, 255, 0)
     rect(0, 400, 700, 600)
     fill(104, 34, 139)
     rect(100, 300, 100, 100)
     fill(191, 62, 255)
     triangle(150, 232, 100, 300, 201, 300)
     fill(255, 255, 255)
     rect(105, 305, 30, 30)
     rect(165, 305, 30, 30)
     fill(255, 174, 185)
     rect(135, 355, 30, 45)
     
     noStroke()
     rect(400, 270, 50, 130)
     fill(124, 252, 0)
     ellipse(403, 265, 60, 60)
     ellipse(440, 265, 60, 60)
     ellipse(420, 245, 60, 60)
     fill(255, 255, 0)
     ellipse(100, 50, 70, 70)
     
     
     
  
  
