import sys
from ship import Ship
from time import sleep
from settings import Settings
from game_stats import GameStats
import pygame
from bullet import Bullet
from alien import Alien
from random import randint
from button import Button
from scoreboard import Scoreboard




class AlienInvasion:
	def __init__(self):

		# def _create_fleet(self):
		# 	alien = Alien(self)
		# 	self.aliens.add(alien)
		
		self.bullets = pygame.sprite.Group() 
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))

		pygame.display.set_caption('Alien Invasion')
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)
		self.game_active = False

		self.play_button = Button(self, 'Play')


		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self._create_fleet()


	def _check_aliens_bottom(self):
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= self.settings.screen_height:
				self._ship_hit()
				break


	def _create_alien(self, x_pos, y_pos):
		new_alien = Alien(self)
		new_alien.x = x_pos
		new_alien.rect.x = x_pos
		new_alien.rect.y = y_pos
		self.aliens.add(new_alien)


	def _fire_bullet(self):
		new_bullet = Bullet(self)
		self.bullets.add(new_bullet)


	def _create_fleet(self):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		current_x, current_y = alien_width, alien_height

		while current_y < (self.settings.screen_height - 3 * alien_height):
			while current_x < (self.settings.screen_width - randint(5, 15) * alien_width):
				self._create_alien(current_x, current_y)
				current_x += 2 * alien_width

			current_x = alien_width
			current_y += 2 * alien_height


	def _ship_hit(self):
		if self.stats.ships_left > 0:
			self.stats.ships_left -= 1

			self.bullets.empty()
			self.aliens.empty()
			self._create_fleet()
			self.ship.center_ship()
			sleep(0.5)
		else:
			self.game_active = False


	def _update_aliens(self):
		self._check_fleet_edges()

		self.aliens.update()

		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
			self._check_aliens_bottom()
			print('Ship hit!!!!!!!!!!!!')


	def _check_fleet_edges(self):
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break
			

	def _change_fleet_direction(self):
		for alien in self.aliens.sprites():
			 alien.move_alien_off_the_wall()

			 alien.rect.y += self.settings.fleet_drop_speed
			 self.settings.fleet_direction *= -1
		

	def _update_screen(self):
		if not self.game_active:
			self.stats.reset_stats()
			self.play_button.draw_button()

		self.screen.fill(self.settings.bg_color)
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.ship.blitme()
		self.aliens.draw(self.screen)
		
		pygame.display.flip()


	def _check_play_button(self, mouse_pos):
		if self.play_button.rect.collidepoint(mouse_pos):
			self.game_active = True


	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)


	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		if event.key == pygame.K_q:
			sys.exit()
		if event.key == pygame.K_SPACE:
			self._fire_bullet()


	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		if event.key == pygame.K_q:
			sys.exit()
		if event.key == pygame.K_SPACE:
			self._fire_bullet()


	def run_game(self):
		self.sb.prep_score()

		while True:
			self._check_events()

			if self.game_active:
			
				self._update_screen()
				self.ship.update()
				self._update_aliens()
				self.bullets.update()
				
			
				collisions = pygame.sprite.groupcollide(
					self.bullets, self.aliens, True, True)
				
				if collisions:
					for aliens in collisions.values():
						self.stats.score += self.settings.alien_points * len(self.aliens)
					self.sb.prep_score()
					self.sb.check_high_score()
				
				if not self.aliens:
					self.bullets.empty()
					self._create_fleet()
					
					self.stats.level += 1
					self.sb.prep_level()





if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()


























