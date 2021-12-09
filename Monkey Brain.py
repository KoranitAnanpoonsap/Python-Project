import pygame
import sys
import random

pygame.init()  # inititalize pygame
# background music
pygame.mixer.init()
pygame.mixer.music.load("D:\\repositories\Python-Project\wii.mp3")
pygame.mixer.music.set_volume(0.03)
pygame.mixer.music.play(-1, 0.0)

#############################################################################
width = 1000
height = 620
screen = pygame.display.set_mode([width, height])
screen.fill([144, 238, 144])
image = pygame.image.load("D:\\repositories\Python-Project\image\monk.jpg")
create_block = True
array_x = [0, 100, 200, 300, 400, 500]
array_y = [0, 100, 200, 300, 400, 500]
hide_block = False
scores = 0
high_score = 0
font = pygame.font.SysFont("Arial", 32)
first_blocks = 1
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
def score():
    final = font.render("Score: " + str(scores), True, (255, 255, 255))
    screen.blit(final, (730, 300))


# highest scores
def highscore():
    global high_score
    if scores > high_score:
        high_score = scores
    final = font.render("Highest Score: " + str(high_score), True, (255, 255, 255))
    screen.blit(final, (700, 200))


# reset the game
def reset():
    global blocks, total_blocks, clicks, scores
    blocks = []
    total_blocks = 0
    clicks = 0
    scores = 0


# correct
def correct():
    global blocks, total_blocks, clicks, scores, create_block, count
    scores += 1
    blocks = []
    total_blocks += 1
    create_block = True
    clicks = 0
    count = 0


# The game
def game():
    global create_block, hide_block, first_blocks, blocks, total_blocks, clicks, num, scores, gameover, count, array_x, array_y, i
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hide_block == False and count >= len(blocks):
                if clicks < len(blocks) and len(blocks) != 1:
                    x, y = event.pos
                    if (
                        blocks[clicks][0] <= x <= blocks[clicks][0] + 100
                        and blocks[clicks][1] <= y <= blocks[clicks][1] + 100
                    ):
                        clicks += 1
                        if clicks == len(blocks):
                            correct()
                    else:
                        gameover = True
                elif clicks < first_blocks:
                    x, y = event.pos
                    if (
                        blocks[0][0] <= x <= blocks[0][0] + 100
                        and blocks[0][1] <= y <= blocks[0][1] + 100
                    ):
                        correct()
                    else:
                        gameover = True
    if hide_block:
        pygame.draw.rect(
            screen,
            (144, 238, 144),
            ((blocks[num][0] + 11, blocks[num][1] + 10), (88, 88)),
        )
        if num + 1 < len(blocks):
            num += 1
            create_block = True
        else:
            num = 0
        hide_block = False
    if create_block:
        if len(blocks) <= total_blocks:
            block_x = random.choice([x for x in range(0, 600, 100) if x in array_x])
            array_x.remove(block_x)
            block_y = random.choice([y for y in range(0, 600, 100) if y in array_y])
            array_y.remove(block_y)
            blocks.append([block_x, block_y])
            if i >= 1:
                array_x = [0, 100, 200, 300, 400, 500]
                array_x.remove(block_x)
                array_y = [0, 100, 200, 300, 400, 500]
                array_y.remove(block_y)
            i += 1
        else:
            array_x = [0, 100, 200, 300, 400, 500]
            array_y = [0, 100, 200, 300, 400, 500]
            i = 0
            monkey = pygame.transform.scale(image, (88, 88))
            screen.blit(monkey, (blocks[num][0] + 11, blocks[num][1] + 10))
            count += 1
            create_block = False
            hide_block = True
    if gameover:
        reset()
        create_block = True
        gameover = False


def main_game():
    while True:
        pygame.time.Clock().tick(1.7)
        screen.fill([144, 238, 144])
        draw()
        game()
        pygame.draw.rect(screen, (144, 238, 144), ((730, 300), (150, 100)))
        score()
        pygame.draw.rect(screen, (144, 238, 144), ((800, 200), (200, 100)))
        highscore()
        pygame.display.update()


def main_menu():
    while True:
        screen.fill([144, 238, 144])
        title = font.render("MONKEY BRAIN", True, (0, 100, 0))
        screen.blit(title, (400, 100))
        pygame.draw.rect(screen, (0, 100, 0), ((420, 250), (150, 100)))
        play = font.render("PLAY", True, (255, 255, 255))
        screen.blit(play, (463, 283))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 420 <= x <= 570 and 250 <= y <= 350:
                    main_game()

        pygame.display.update()


main_menu()
