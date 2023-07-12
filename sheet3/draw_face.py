from gasp import*

begin_graphics()

def drawface(x,y):
    Circle((x,y), 40)
    Circle ((x-20,y),5)
    Circle((x+20,y),5)
    Line((x,y+10), (x-10, y-10))
    Line((x-10,y-10),(x+10,y-10))
    Arc((x,y), 30, 225, 315)
    
for col in range(40, 700,80):
    for row in range(40, 300, 80):
        drawface(col,row)

update_when('key_pressed')
end_graphics()