class Settings:
	

	def __init__(self):
		self.screen_width = 1199
		self.screen_height = 700
		self.bg_color = (255, 255, 255)
		self.bullet_speed = 2.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.alien_speed = 1
		self.fleet_drop_speed = 50
		self.fleet_direction = 1
		self.ship_limit = 3
		self.speedup_scale = 1.01
		self.initialize_dynamic_settings()
		self.score_scale = 1.5
		print(self.alien_points)

		
	def initialize_dynamic_settings(self):
		self.ship_speed = 1.5
		self.bullet_speed = 2.5
		self.alien_speed = 0.1
		self.fleet_direction = 1
		self.alien_points = 50


	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)







