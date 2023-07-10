from gasp import*

begin_graphics()

Circle((300,200),100)
Circle((250, 200), 20)
Circle((350,200),20)
Line((250,150), (300,170))
Line((250,150), (300,150))
Arc((300,150), 30, 225, 315)
Arc((250,220), 30, 180, 0)
Arc((350,220),30,180,0)

update_when('key_pressed')
end_graphics()
