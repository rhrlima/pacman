from dependencies import *


class Sprite:

	def __init__(self, image, r=1, c=1):
		
		img = pg.image.load(image).convert()
		
		self.width  = img.get_width()  // c
		self.height = img.get_height() // r

		self.rows   = r
		self.nframes = c
		
		self.frames  = []
		
		self.create_frames(img)

	def create_frames(self, image):
		for row in range(self.rows):
			for col in range(self.nframes):
				aux = image.subsurface( (col * self.width, row * self.height, self.width, self.height) )
				aux.set_colorkey(ALPHA_COLOR)
				self.frames.append(aux)

	def get_frame(self, r, c):
		if r < self.rows and c < self.nframes:
			return self.frames[r * self.nframes + c]
		return None

	def draw(self, surface, x=0, y=0, i=0, j=0):
		index = i * self.nframes + j
		surface.blit(self.frames[index], (x, y))


sprites = {}

def load_sprites():
	sprites['pacman'] = Sprite('images/pacman.png', 4, 4)
	sprites['blinky'] = Sprite('images/blinky.png', 4, 2)
	sprites['pinky']  = Sprite('images/pinky.png' , 4, 2)
	sprites['inky']   = Sprite('images/inky.png'  , 4, 2)
	sprites['clyde']  = Sprite('images/clyde.png' , 4, 2)
	sprites['ghost']  = Sprite('images/ghost.png' , 1, 4)
	sprites['coins']  = Sprite('images/coins.png' , 1, 2)
	sprites['text']   = Sprite('images/text.png'  , 4, 13)
	print("All sprites loaded.")


def get_sprite(sprite_key):
	if len(sprites.keys()) == 0:
		return None
	return sprites[sprite_key]


if __name__ == "__main__":
	print("This file is not supposed to be run directly.")
