from dependencies import *


class Block:

	def __init__(self, spr=None, x=0, y=0, w=TILE_SIZE, h=TILE_SIZE):
		self.x = x
		self.y = y
		
		self.width  = w
		self.height = h

		self.visible = True
		self.solid   = True
		
		self.sprite = spr
		self.color	= PINK

		self.speed 		 = 0
		self.direction	 = 0
		self.curr_frame  = 0
		self.last_update = 0
		self.ani_speed 	 = 0

	def update(self, seconds):
		if self.sprite is not None and self.ani_speed > 0:
			self.last_update += seconds
			if self.last_update >= self.ani_speed:
				self.curr_frame = (self.curr_frame + 1) % self.sprite.nframes
				self.last_update = 0

	def draw(self, surface):
		if self.visible:
			if self.sprite is not None:
				aux = 0
				if self.direction < self.sprite.rows:
					aux = self.direction
				self.sprite.draw(surface, self.x, self.y, aux, self.curr_frame)
				#pg.draw.rect( surface, (255, 0, 0), self.get_rect(), 2)
			else:
				pg.draw.rect( surface, self.color, Rect((self.x, self.y),(self.width, self.height)), 2)

	def set_sprite(self, spr):
		self.sprite = spr
		self.width  = self.sprite.width
		self.height = self.sprite.height
		self.curr_frame  = 0
		self.last_update = 0

	def get_rect(self):
		return Rect(self.x, self.y, self.width, self.height)

	def intersects(self, entity, direction=None):
		if direction is None:
			direction = self.direction
		self_rect = None
		if direction == K_UP:
			self_rect = Rect( (self.x, self.y-self.speed), (self.width, self.height) )
		elif direction == K_RIGHT:
			self_rect = Rect( (self.x+self.speed, self.y), (self.width, self.height) )
		elif direction == K_LEFT:
			self_rect = Rect( (self.x-self.speed, self.y), (self.width, self.height) )
		elif direction == K_DOWN:
			self_rect = Rect( (self.x, self.y+self.speed), (self.width, self.height) )

		if self_rect.colliderect(entity.get_rect()):
			return True
		return False


class Entity(Block):

	def __init__(self, sprite=None, x=0, y=0, w=TILE_SIZE, h=TILE_SIZE):
		super(Entity, self).__init__(sprite, x, y, w, h)
		self.direction = K_RIGHT
		self.next_direction = self.direction

	def update(self, seconds):
		super(Entity, self).update(seconds)

		if self.direction == K_UP:
			self.y -= self.speed
		elif self.direction == K_RIGHT:
			self.x += self.speed
		elif self.direction == K_LEFT:
			self.x -= self.speed
		elif self.direction == K_DOWN:
			self.y += self.speed

		if self.x + self.width < 0:
			self.x = WINDOW_W
		elif self.x > WINDOW_W:
			self.x = -self.width

	def collides_with(self, other):
		if self.intersects(other):
			if self.direction == K_UP:
				self.y = other.y + other.height
			elif self.direction == K_RIGHT:#right
				self.x = other.x - self.width
			elif self.direction == K_LEFT:#left
				self.x = other.x + other.width
			elif self.direction == K_DOWN:#bottom
				self.y = other.y - self.height


class Player(Entity):

	def __init__(self):
		spr = get_sprite('pacman')
		super(Player, self).__init__(spr)
		self.speed = 4
		self.ani_speed = 0.1
		self.sprite_dict = {K_UP: 0, K_RIGHT: 1, K_LEFT: 2, K_DOWN: 3}

	def draw(self, surface):
		if self.visible:
			self.sprite.draw(surface, self.x, self.y, self.sprite_dict[self.direction], self.curr_frame)
			#pg.draw.rect( surface, (255, 0, 0), self.get_rect(), 2)


class Enemy(Entity):

	def __init__(self, name):
		spr  = get_sprite(name)
		super(Enemy, self).__init__(spr, TILE_SIZE, TILE_SIZE + SCORE_OFF)
		self.x = TILE_SIZE * 10
		self.y = TILE_SIZE * 15
		self.speed = 4
		self.direction = K_UP
		self.ani_speed = 0.1

		self.starting = False

	def pick_direction(self):
		if not self.starting:
			rand = randint(0, 3)
			if rand == 0 and self.direction != K_DOWN:
				self.next_direction = K_UP
			elif rand == 1 and self.direction != K_LEFT:
				self.next_direction = K_RIGHT
			elif rand == 2 and self.direction != K_RIGHT:
				self.next_direction = K_LEFT
			elif rand == 3 and self.direction != K_UP:
				self.next_direction = K_DOWN


class SmallCoin(Entity):

	def __init__(self, x, y):
		spr = get_sprite('coins')
		super(SmallCoin, self).__init__(spr, x, y)

	def get_rect(self):
		x = self.x + self.width  / 2 - 2
		y = self.y + self.height / 2 - 2
		return Rect(x, y, 4, 4)


class BigCoin(Entity):

	def __init__(self, x, y):
		spr = get_sprite('coins')
		super(BigCoin, self).__init__(spr, x, y)
		self.curr_frame = 1
		
	def get_rect(self):
		x = self.x + self.width  / 2 - 4
		y = self.y + self.height / 2 - 4
		return Rect(x, y, 8, 8)


class Score:

	def __init__(self):
		self.score_text = "score"
		self.score = 0

	def draw(self, surface):
		display_text("Score", surface, 0, 0)
		display_text(str(self.score), surface, 0, 8)

	def add_points(self, points):
		self.score += points


if __name__ == "__main__":
	print("This file is not supposed to be run directly.")