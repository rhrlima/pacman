from dependencies import *


class App:

	def __init__(self):
		
		pg.init()
		pg.display.set_caption("PacMan")		

		self.width 	 = WINDOW_W
		self.height  = WINDOW_H
		self.fps 	 = 30
		self.running = False
		self.clock	 = None
		self.surface = None

		self.score 	 = None

		self.player  = None
		self.enemies = []
		self.coins   = []
		
		self.map  	 = None

	def setup(self):
		self.surface = pg.display.set_mode( (self.width, self.height), pg.HWSURFACE )
		self.clock = pg.time.Clock()

		pg.key.set_repeat(15, 15)
		load_sprites()
		load_text()

		self.score = Score()

		self.player = Player()
		self.player.x = TILE_SIZE * 10
		self.player.y = TILE_SIZE * 22

		self.enemies.append( Enemy('blinky') )
		self.enemies.append( Enemy('pinky') )
		self.enemies.append( Enemy('inky') )
		self.enemies.append( Enemy('clyde') )

		self.map = TiledMap('images/map.tmx')

		self.running = True

	def event(self, event):
		
		if event.type == QUIT:
			self.running = False

		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				self.running = False		

		if event.type == KEYDOWN:
			if event.key == K_UP or event.key == K_RIGHT or event.key == K_LEFT or event.key == K_DOWN:
				self.player.next_direction = event.key

	def update(self, seconds):

		if self.map.can_move(self.player, self.player.next_direction):
			self.player.direction = self.player.next_direction

		self.player.update(seconds)
		self.map.update(self.player)

		for coin in self.map.coins:
			if self.player.intersects(coin):
				self.map.coins.remove(coin)
				if isinstance(coin, SmallCoin):
					self.score.add_points(10)
				elif isinstance(coin, BigCoin):
					self.score.add_points(100)
					#activate big coin effect

		for enemy in self.enemies:
			if not enemy.starting:
				for i in range(4):
					enemy.pick_direction()
					if self.map.can_move(enemy, enemy.next_direction):
						enemy.direction = enemy.next_direction
						break
			enemy.update(seconds)
			self.map.update(enemy)

	def draw(self):
		self.surface.fill( BLACK )
		self.map.draw(self.surface, (0, 1))
		for enemy in self.enemies:
			enemy.draw(self.surface)
		self.player.draw(self.surface)
		self.score.draw(self.surface)
		pg.display.flip()

	def teardown(self):
		pg.quit()
		quit()

	def execute(self):
		self.setup()
		while self.running:
			seconds = self.clock.tick(self.fps) / 1000
			for event in pg.event.get():
				self.event(event)
			self.update(seconds)
			self.draw()
		self.teardown()

if __name__ == '__main__':
	game = App()
	game.execute()