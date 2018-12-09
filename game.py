import pygame
pygame.init()

screen_height = 400
screen_width = 400
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
#bg = pygame.image.load('bg.jpg')
#char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

def refresh_screen():
	pygame.display.update()

class Player():
	def __init__(self, x, y, width, height, velocity, stand):
		self.x = x
		self.y = y
		self.width = width
		self.heigh = height
		self.velocity = velocity
		self.isJump = False
		self.jumpCount = 10
		self.left = False
		self.right = False
		self.walkCount = 0
		self.stand_image = stand

	def move_player(self, screen):
		if self.left:
			screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
			self.walkCount += 1
			self.x -= self.velocity
			self.left = False

		elif self.right:
			screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
			self.walkCount += 1
			self.x += self.velocity
			self.right = False

		else:
			screen.blit(self.stand_image, (self.x,self.y))

	def jump_player(self, screen):
		if not(self.isJump):
			if keys[pygame.K_SPACE]:
				self.isJump = True
				self.right = False
				self.left = False
				self.walkCount = 0
		else:
			if self.jumpCount >= -10:
				neg = 1
				if self.jumpCount < 0:
					neg = -1
				self.y -= (self.jumpCount ** 2) * 0.5 * neg
				self.jumpCount -= 1
			else:
				self.isJump = False
				self.jumpCount = 10

def redrawGameWindow():
	pygame.display.update()
	screen.fill((0, 0, 0))

#mainLoop
running = True

# screen defined outside of function so it is global
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Spacey Gamey")

player = Player(300, 200, 64, 64, 5, pygame.image.load('standing.png'))

while(running):
	redrawGameWindow()
	clock.tick(27)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	keys = pygame.key.get_pressed()

	if player.walkCount + 1 >= 27:
		player.walkCount = 0

	if not(player.isJump):
		if keys[pygame.K_SPACE]:
			player.isJump = True
	else:	
		player.jump_player(screen)

	if keys[pygame.K_LEFT] and 0 < player.x:
		player.left = True
		player.move_player(screen)

	elif keys[pygame.K_RIGHT] and player.x < screen_width - player.width:
		player.right = True
		player.move_player(screen)

	else:
		player.move_player(screen)




