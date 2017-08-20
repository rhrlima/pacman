from dependencies import *

source_image = None

alphabet = {}

def load_text():
	global source_image, alphabet
	source_image = sprites['text']
	
	#Mapping
	#Numbers
	alphabet['0'] = source_image.get_frame(0, 0)
	alphabet['1'] = source_image.get_frame(0, 1)
	alphabet['2'] = source_image.get_frame(0, 2)
	alphabet['3'] = source_image.get_frame(0, 3)
	alphabet['4'] = source_image.get_frame(0, 4)
	alphabet['5'] = source_image.get_frame(0, 5)
	alphabet['6'] = source_image.get_frame(0, 6)
	alphabet['7'] = source_image.get_frame(0, 7)
	alphabet['8'] = source_image.get_frame(0, 8)
	alphabet['9'] = source_image.get_frame(0, 9)

	#Letters
	alphabet['a'] = source_image.get_frame(1, 0)
	alphabet['b'] = source_image.get_frame(1, 1)
	alphabet['c'] = source_image.get_frame(1, 2)
	alphabet['d'] = source_image.get_frame(1, 3)
	alphabet['e'] = source_image.get_frame(1, 4)
	alphabet['f'] = source_image.get_frame(1, 5)
	alphabet['g'] = source_image.get_frame(1, 6)
	alphabet['h'] = source_image.get_frame(1, 7)
	alphabet['i'] = source_image.get_frame(1, 8)
	alphabet['j'] = source_image.get_frame(1, 9)
	alphabet['k'] = source_image.get_frame(1, 10)
	alphabet['l'] = source_image.get_frame(1, 11)
	alphabet['m'] = source_image.get_frame(1, 12)
	alphabet['n'] = source_image.get_frame(2, 0)
	alphabet['o'] = source_image.get_frame(2, 1)
	alphabet['p'] = source_image.get_frame(2, 2)
	alphabet['q'] = source_image.get_frame(2, 3)
	alphabet['r'] = source_image.get_frame(2, 4)
	alphabet['s'] = source_image.get_frame(2, 5)
	alphabet['t'] = source_image.get_frame(2, 6)
	alphabet['u'] = source_image.get_frame(2, 7)
	alphabet['v'] = source_image.get_frame(2, 8)
	alphabet['w'] = source_image.get_frame(2, 9)
	alphabet['x'] = source_image.get_frame(2, 10)
	alphabet['y'] = source_image.get_frame(2, 11)
	alphabet['z'] = source_image.get_frame(2, 12)

	#Special caracters
	alphabet[' '] = source_image.get_frame(3, 0)
	alphabet['-'] = source_image.get_frame(3, 1)
	alphabet['/'] = source_image.get_frame(3, 2)
	alphabet['\"'] = source_image.get_frame(3, 3)
	alphabet['.'] = source_image.get_frame(3, 4)
	alphabet['>'] = source_image.get_frame(3, 5)
	alphabet['@'] = source_image.get_frame(3, 6)
	print("Alphabet loaded.")

def text_to_image(text):
	img_text = []
	text = text.lower()
	for letter in text:
		img_text.append(alphabet[letter])
	return img_text

def display_text(text, surface, x=0, y=0):
	img_text = text_to_image(text)
	tx = x
	for caracter in img_text:
		surface.blit(caracter, (tx, y))
		tx += TILE_SIZE/2


if __name__ == "__main__":
	print("This file is not supposed to be run directly.")