import pygame
from random import randint
pygame.init()

WIDTH = 500
HEIGHT = 500

WHITE = (255, 255, 255)
LIGHT_BLUE = (200, 200, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(LIGHT_BLUE)

clock = pygame.time.Clock()
FPS = 90

class TextArea():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def set_text(self, text, fsize=17, text_color=BLACK):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True, text_color)

    def draw(self, shift_x=10, shift_y=10):
        pygame.draw.rect(window, self.fill_color, self.rect)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

quest_card = TextArea(120, 100, 300, 70, GREEN)
quest_card.set_text("Питання", 75)

answer_card = TextArea(120, 248, 300, 90, RED)
answer_card.set_text("Відповідь", 75)

quest_card.draw(10, 10)
answer_card.draw(10, 10)
 
a = 28

while True:
    for event in pygame.event.get():
        #if event.type == pygame.QUIT:
        #       exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                num = randint(1, 10)
                if num == 1:
                    quest_card.set_text("Що вивчаєш в Logika?", a)
                if num == 2:
                    quest_card.set_text("Якою мовою говорять у Франції?", a)
                if num == 3:
                    quest_card.set_text("Що росте на яблуні?", a)
                if num == 4:
                    quest_card.set_text("На честь кого названо місто Вашингтон?", a)
                if num == 5:
                    quest_card.set_text("Чого Нью-Йорк - Нью-Йорк?", a)
                if num == 6:
                    quest_card.set_text("Де знаходиться Україна?", a)  
                if num == 7:
                    quest_card.set_text("Не лежи на печі...", a)
                if num == 8:
                    quest_card.set_text("RGB це", a)
                if num == 9:
                    quest_card.set_text("Ніколи не кажи гоп...", a)
                if num == 10:
                    quest_card.set_text("Як ти?", a)  
            if event.key == pygame.K_a:
                num = randint(1, 10)
                if num == 1:
                    answer_card.set_text("Phyton", a)
                if num == 2:
                    answer_card.set_text("Французькою", a)
                if num == 3:
                    answer_card.set_text("Яблука", a)
                if num == 4:
                    answer_card.set_text("На честь Вашингтона", a)
                if num == 5:
                    answer_card.set_text("Бо новий Йорк", a)
                if num == 6:
                    answer_card.set_text("В східній Європі", a)
                if num == 7:
                    answer_card.set_text("Бо не з'їси калачі", a)
                if num == 8:
                    answer_card.set_text("Red, Blue, Green", a)
                if num == 9:
                    answer_card.set_text("Поки не перестрибнув", a)
                if num == 10:
                    answer_card.set_text("ДОБРЕ!!!", a)

    quest_card.draw(10, 10)
    answer_card.draw(10, 10)



    clock.tick(FPS)
    pygame.display.update()
