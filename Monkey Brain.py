import pygame
import sys
import random

pygame.init()  # inititalize pygame

# soundeffect
def soundeffect():
    pygame.mixer.Channel(0).play(
        pygame.mixer.Sound("D:\\repositories\Python-Project\hitsound.WAV")
    )
    pygame.mixer.Channel(0).set_volume(0.03)


#############################################################################
width = 1000
height = 620
screen = pygame.display.set_mode([width, height])
screen.fill([144, 238, 144])
image = pygame.image.load("D:\\repositories\Python-Project\image\monk.jpg")
create_block = True
list_x = [0, 100, 200, 300, 400, 500]
list_y = [0, 100, 200, 300, 400, 500]
hide_block = False
level = 0
high_level = 0
font = pygame.font.SysFont("Arial", 32)
font_2 = pygame.font.SysFont("Arial", 80)
blocks = []
total_blocks = 0
clicks = 0
num = 0
count = 0
i = 0
gameover = False

# the grid
def draw():
    for i in range(7):
        pygame.draw.rect(
            screen,
            (0, 100, 0),
            ((100 * i, 0), (10, 600)),
        )
        pygame.draw.rect(
            screen,
            (0, 100, 0),
            ((0, 100 * i), (610, 10)),
        )


# scores
def levels():
    final = font.render("Level: " + str(level), True, (255, 255, 255))
    screen.blit(final, (730, 300))


# highest scores
def highlevel():
    global high_level
    if level > high_level:
        high_level = level
    final = font.render("Highest Level: " + str(high_level), True, (255, 255, 255))
    screen.blit(final, (700, 200))


def highlevel_restart():
    global high_level
    if level > high_level:
        high_level = level
    final = font_2.render("Highest Level: " + str(high_level), True, (0, 100, 0))
    screen.blit(final, (280, 130))


# reset the game
def reset():
    global blocks, total_blocks, clicks, level
    blocks = []
    total_blocks = 0
    clicks = 0
    level = 0


# correct
def correct():
    global blocks, total_blocks, clicks, level, create_block, count
    level += 1
    blocks = []
    total_blocks += 1
    create_block = True
    clicks = 0
    count = 0


# restart
def restart():
    global create_block
    while True:
        reset()
        create_block = True
        screen.fill([144, 238, 144])
        highlevel_restart()
        pygame.draw.rect(screen, (0, 100, 0), ((420, 250), (150, 100)))
        play = font.render("RESTART", True, (255, 255, 255))
        screen.blit(play, (435, 283))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 420 <= x <= 570 and 250 <= y <= 350:
                    soundeffect()
                    main_game()

        pygame.display.update()


def game():
    global create_block, hide_block, blocks, total_blocks, clicks, num, scores, gameover, count, list_x, list_y, i
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if hide_block == False and count == len(blocks):
                if clicks < len(blocks):
                    x, y = event.pos
                    if (
                        blocks[clicks][0] <= x <= blocks[clicks][0] + 100
                        and blocks[clicks][1] <= y <= blocks[clicks][1] + 100
                    ):
                        soundeffect()
                        clicks += 1
                        if clicks == len(blocks):
                            correct()
                    else:
                        restart()
    if hide_block:
        pygame.draw.rect(
            screen,
            (144, 238, 144),
            ((blocks[num][0] + 11, blocks[num][1] + 10), (88, 88)),
        )
        if num + 1 != len(blocks):
            num += 1
            create_block = True
        else:
            num = 0
        hide_block = False
    if create_block:
        if len(blocks) <= total_blocks:
            block_x = random.choice([x for x in range(0, 600, 100) if x in list_x])
            list_x.remove(block_x)
            block_y = random.choice([y for y in range(0, 600, 100) if y in list_y])
            list_y.remove(block_y)
            blocks.append([block_x, block_y])
            if i >= 1:
                list_x = [0, 100, 200, 300, 400, 500]
                list_x.remove(block_x)
                list_y = [0, 100, 200, 300, 400, 500]
                list_y.remove(block_y)
            i += 1
        else:
            list_x = [0, 100, 200, 300, 400, 500]
            list_y = [0, 100, 200, 300, 400, 500]
            i = 0
            monkey = pygame.transform.scale(image, (88, 88))
            screen.blit(monkey, (blocks[num][0] + 11, blocks[num][1] + 10))
            soundeffect()
            count += 1
            create_block = False
            hide_block = True


def main_game():
    while True:
        pygame.time.Clock().tick(2)
        screen.fill([144, 238, 144])
        draw()
        game()
        levels()
        highlevel()
        pygame.display.update()


def main_menu():
    while True:
        screen.fill([144, 238, 144])
        title = font_2.render("MONKEY BRAIN", True, (0, 100, 0))
        screen.blit(title, (250, 100))
        pygame.draw.rect(screen, (0, 100, 0), ((420, 250), (150, 100)))
        play = font.render("PLAY", True, (255, 255, 255))
        screen.blit(play, (463, 283))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 420 <= x <= 570 and 250 <= y <= 350:
                    soundeffect()
                    main_game()

        pygame.display.update()


main_menu()
