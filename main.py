import pygame
pygame.init()

back = (200, 255, 255)
screen_width, screen_height = 500, 500
mw = pygame.display.set_mode((screen_width, screen_height))
mw.fill(back)
clock = pygame.time.Clock()
dx = 3
dy = 3

go = False

move_right = False
move_left = False   
platform_x = 200
platform_y = 330

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    
    def outline(self, outline_color, thickness):
        pygame.draw.rect(mw, outline_color, self.rect, thickness)
    
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont("verdana", fsize).render(text, True, text_color)
    
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

ball = Picture("ball.png", 220, 230, 50, 50)
platform = Picture("platform.png", 200, 300, 100, 30)

start_x = 5
start_y = 5
count = 9

monsters = []
for i in range(3):
    y = start_y + (55* i)
    x = start_x + (27.5* i)
    for j in range(count):
        d = Picture ("enemy.png", x, y, 50, 50)
        monsters.append(d)
        x = x + 55
    count = count - 1


while not go:
    ball.fill()
    platform.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False

    if move_right:
        platform.rect.x += 3
    if move_left:
        platform.rect.x -= 3
    ball.rect.x += dx
    ball.rect.y += dy 
    if ball.rect.y < 0:
        dy *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        dx *= -1
    if ball.rect.y > 350:
        time_text = Label(150, 150, 50, 50, back)
        time_text.set_text("ТИ БОТ АХАХ", 60, (255, 0, 0))
        time_text.draw(10, 10)
        go = True
    if len(monsters) == 0:
        time_text = Label(150, 150, 50, 50, back)
        time_text.set_text("ТИ НЕ БОТ", 60, (255, 0, 0))
        time_text.draw(10, 10)
        go = True
    if ball.rect.colliderect(platform.rect):
        dy *= -1
    for m in monsters:
        m.draw()
        if m.rect.colliderect(ball.rect):
            monsters.remove(m)
            m.fill()
            dy *= -1


    platform.draw()
    ball.draw()

    pygame.display.update()
    clock.tick(40)
