from dependencies import *

"""
if camera x > map x move camera with player
if camera x < map x: dont move camera
"""

class TiledMap:

	def __init__(self, file_name):

		tm = load_pygame(file_name)
		
		self.tmx_data = tm

		self.width  = tm.width
		self.height = tm.height

		self.tile_width  = tm.tilewidth
		self.tile_height = tm.tileheight

		self.maze    = []
		self.coins   = []
		self.corners = []
		self.walls   = []
		self.grid    = []

		self.none_block = Block(None, 0, 0)

		temp = tm.get_layer_by_name('maze')
		for x, y, img in temp.tiles():
			self.maze.append( (x * self.tile_width, y * self.tile_height + SCORE_OFF, img) )

		temp = tm.get_layer_by_name('small_coins')
		for x, y, img in temp.tiles():
			self.coins.append( SmallCoin(x * self.tile_width, y * self.tile_height + SCORE_OFF) )

		temp = tm.get_layer_by_name('big_coins')
		for x, y, img in temp.tiles():
			self.coins.append( BigCoin(x * self.tile_width, y * self.tile_height + SCORE_OFF) )

		temp = tm.get_layer_by_name('corners')
		for x, y, img in temp.tiles():
			self.corners.append( (x * self.tile_width, y * self.tile_height + SCORE_OFF) )

		for i in range(self.height):
			self.grid.append([])
			for j in range(self.width):
				self.grid[i].append(self.none_block)

		temp = tm.get_layer_by_name('walls')
		for x, y, img in temp.tiles():
			block = Block(None, x * self.tile_width, y * self.tile_height + SCORE_OFF)
			self.grid[y][x] = block
			self.walls.append( block )

	def update(self, entity):
		#revisar
		for block in self.walls:
			entity.collides_with(block)

	def draw(self, surface, layers=(0, 1)):
		if layers[0]:
			for wall in self.walls:
				if wall is not None:
					wall.draw(surface)
		else:
			for x, y, image in self.maze:
				surface.blit(image, (x, y))

		if layers[1]:
			for coin in self.coins:
				coin.draw(surface)

	def get_block(self, i, j, direction=None):
		i -= 2
		if i >= 0 and i < self.height and j >= 0 and j < self.width:
			if direction == K_UP:
				return self.grid[i-1][j]
			elif direction == K_RIGHT:
				return self.grid[i][j+1]
			elif direction == K_LEFT:
				return self.grid[i][j-1]
			elif direction == K_DOWN:
				return self.grid[i+1][j]
			else:
				return self.grid[i][j]
		return self.none_block

	def can_move(self, entity, direction):
		ex = entity.x % TILE_SIZE
		ey = entity.y % TILE_SIZE		
		ei = entity.y // TILE_SIZE
		ej = entity.x // TILE_SIZE
		if ei >= 0 and ej >=0 and ei < WINDOW_TILE_H-1 and ej < WINDOW_TILE_W-1:
			if ex == 0 and ey == 0 and not entity.intersects(self.get_block(ei, ej, direction), direction):
				return True
		return False

if __name__ == "__main__":
	print("This file is not supposed to be run directly.")