import pygame
import random
 
pygame.init()
 
dis_width = 600
dis_height = 400
fruit_color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
snake_color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15

fun_value = random.randint(1, 100)
 
font_style = pygame.font.SysFont("comicsansms", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, (255,255,255))
    dis.blit(value, [0, 0])
 
 
def our_snake(snake_block, snake_list, snake_color):
    if fun_value <= 99:
        for x in snake_list:
            pygame.draw.rect(dis, snake_color, [x[0], x[1], snake_block, snake_block])
    elif fun_value == 100:
        for x in snake_list:
            pygame.draw.rect(dis, (random.randint(1,255),random.randint(1,255),random.randint(1,255)), [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop(fruit_color, snake_color):
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill((0,0,0))
            message("You Lost! Press C-play again or Q-quit", (255,0,0))
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        fruit_color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
                        snake_color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
                        gameLoop(fruit_color, snake_color)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill((0,0,0))
        if fun_value <= 99:
            pygame.draw.rect(dis, fruit_color, [foodx, foody, snake_block, snake_block])
        elif fun_value == 100:
            pygame.draw.rect(dis, (random.randint(1,255),random.randint(1,255),random.randint(1,255)), [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List, snake_color)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            fruit_color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop(fruit_color, snake_color)