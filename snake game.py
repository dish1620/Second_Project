import random
import pygame
import os
pygame.mixer.init()

pygame.init()

#back img

y = (115, 255, 255)
white = (255, 255, 255)
pink = (255, 240, 230)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

bging = pygame.image.load("sss.jpg")
bging = pygame.transform.scale(bging,(screen_width, screen_height)).convert_alpha()
start = pygame.image.load("Ssnake.jpg")
start = pygame.transform.scale(start,(screen_width, screen_height)).convert_alpha()
end = pygame.image.load("S2K.jpg")
end = pygame.transform.scale(end,(screen_width, screen_height)).convert_alpha()



pygame.display.set_caption("Snake_With_Dishu")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, colour, x, y):
    screen_text= font.render(text, True, colour)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, colour,snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, colour, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(pink)
        gameWindow.blit(start,(0, 0))
        #text_screen("Welcome to Snake_With_Dishu", black, 180, 280)
        text_screen("Press Space Bar to Play", red, 70, 400)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("back.mp3")
                    pygame.mixer.music.play(-1)

                    game_loop()
        pygame.display.update()

        clock.tick(30)


def game_loop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 45
    snake_size = 20
    fps = 30
    velocity_x = 0
    velocity_y = 0
    score = 0
    food_x = random.randint(10, screen_width )
    food_y = random.randint(10, screen_height )
    init_velocity = 5

    snake_list = []
    snake_len = 1
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")

    with open("highscore.text", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:

            with open("highscore.text", "w") as f:
                f.write(str(highscore))

            gameWindow.fill(y)
            gameWindow.blit(end,(0,0))
            text_screen(" Press Enter To Continue", red, 420, 290)

            text_screen("Final score::" + str(score), black, 450, 150)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()


        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x =  init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y =0

                    if event.key == pygame.K_UP:
                        velocity_y =  - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key== pygame.K_q:
                        score +=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<11 and abs(snake_y - food_y)<11:
                score +=10
                food_x = random.randint(10, screen_width / 2)
                food_y = random.randint(10, screen_height / 3)
                snake_len +=5
                if score>int(highscore):
                    highscore = score

            gameWindow.fill(white)
            gameWindow.blit(bging, (0, 0))
            text_screen("score::" + str(score)+ "   Highscore: " + str(highscore), black, 5, 5)
            #pygame.draw.rect(gameWindow, green, [snake_x, snake_y, snake_size, snake_size])
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)


            if len(snake_list)>snake_len:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True


                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
            if snake_x <0 or snake_x >screen_width or snake_y <0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()



            plot_snake(gameWindow, green, snake_list, snake_size )
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()




