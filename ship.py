import pygame

class Ship:


	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.rect.x = self.screen_rect.x
		self.rect.bottom = self.screen_rect.bottom
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
		self.moving_right = False
		self.moving_left = False

	def blitme(self):
		self.screen.blit(self.image, self.rect)


	def center_ship(self):
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.screen_rect.x)


	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		self.rect.x = self.x

