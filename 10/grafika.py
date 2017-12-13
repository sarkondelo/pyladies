import math
import pyglet
window = pyglet.window.Window()

def tik(dt):
	print(dt)
	had.x = had.x + dt * 40
	had.y = had.y + dt * 40
	had.rotation = had.rotation + dt * 80
pyglet.clock.schedule_interval(tik, 1/30)

def zpracuj_text(text):
	print(text)
	had.x = 150

obrazek = pyglet.image.load('snake.png')
obrazek2 = pyglet.image.load('mys.png')
had = pyglet.sprite.Sprite(obrazek)

def zamen(dt):
	had.image = obrazek2
	pyglet.clock.schedule_once(zamen_zpatky, 2)
def zamen_zpatky(dt):
	had.image = obrazek
	pyglet.clock.schedule_once(zamen, 1)

pyglet.clock.schedule_once(zamen, 1)

def vykresli():
	window.clear()
	had.draw()

def klik(x, y, tlacitko, mod):
	had.x = x
	had.y = y
	print(tlacitko)
	print(mod)

window.push_handlers(
	on_text=zpracuj_text,
	on_draw=vykresli,
	on_mouse_press=klik,
)

print(zpracuj_text)


pyglet.app.run() #
print('Hotovo!')

