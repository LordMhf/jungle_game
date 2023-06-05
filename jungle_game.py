import pygame

pygame.init()
Right_walking = [pygame.image.load('./right_left/R1.png'), pygame.image.load('./right_left/R2.png'),
                 pygame.image.load('./right_left/R3.png'),
                 pygame.image.load('./right_left/R4.png'), pygame.image.load('./right_left/R5.png'),
                 pygame.image.load('./right_left/R6.png'),
                 pygame.image.load('./right_left/R7.png'), pygame.image.load('./right_left/R8.png'),
                 pygame.image.load('./right_left/R9.png')]
Left_walking = [pygame.image.load('./right_left/L1.png'), pygame.image.load('./right_left/L2.png'),
                pygame.image.load('./right_left/L3.png'),
                pygame.image.load('./right_left/L4.png'), pygame.image.load('./right_left/L5.png'),
                pygame.image.load('./right_left/L6.png'),
                pygame.image.load('./right_left/L7.png'), pygame.image.load('./right_left/L8.png'),
                pygame.image.load('./right_left/L9.png')]
rocks = [pygame.image.load('./rocks/1.png'), pygame.image.load('./rocks/2.png'), pygame.image.load('./rocks/3.png'),
         pygame.image.load('./rocks/4.png'),
         pygame.image.load('./rocks/5.png'), pygame.image.load('./rocks/6.png'), pygame.image.load('./rocks/7.png'),
         pygame.image.load('./rocks/8.png'),
         pygame.image.load('./rocks/9.png')]

bgs = [pygame.transform.scale(pygame.image.load('jungle_day.jpg'), (1450, 750)),
       pygame.transform.scale(pygame.image.load('jungle_evening.jpg'), (1450, 750)),
       pygame.transform.scale(pygame.image.load('jungle_night.jpg'), (1450, 750))]

width = 120
height = 180

for i in range(len(Right_walking)):
    Right_walking[i] = pygame.transform.scale(Right_walking[i], (width, height))
    Left_walking[i] = pygame.transform.scale(Left_walking[i], (width, height))

char = pygame.image.load('standing.png')
char = pygame.transform.scale(char, (width, height))

run = True

isJump = False
jumpCount = 10

speed = 30
left = False
right = False
walk_count = 0
win = pygame.display.set_mode((1450, 750))
pygame.display.set_caption("googlegame")

char_x = 20
char_y = 750 - (110 + height)

change_pos = 3
ran = 0

rocks_x = [1450]
rocks_y = 450
rocks_speed = 20
rock_line2 = 720
rock_line1 = 700

score = 0
n = 0


def rock_movement(a=3):
    global rocks_speed, score, ran
    rock_out = False
    for r in rocks_x:
        if len(rocks_x) < a and r in range(rock_line1, rock_line2):
            rock_out = True
    if rock_out:
        rocks_x.append(1450)
    for r in rocks_x:
        if r - rocks_speed >= -200:
            rocks_x[rocks_x.index(r)] -= rocks_speed
        else:
            rocks_x.remove(r)
            score += 1
            if ran + 1 < 9:
                ran += 1
            else:
                ran = 1


def game_over():
    global run
    for r in rocks_x:
        if char_x in range(r, r + 200) or char_x + width in range(r, r + 233):
            if char_y in range(rocks_y, 750):
                run = False


def draw_game():
    global walk_count, n, change_pos, rocks_speed
    if score == change_pos:
        change_pos += change_pos
        if rocks_speed + 5 <= 35:
            rocks_speed += 5
        if n + 1 > 2:
            n = 0
        else:
            n += 1

    win.blit(bgs[n], (0, 0))
    for r in rocks_x:
        win.blit(rocks[ran], (r, rocks_y))

    if walk_count + 1 >= 27:
        walk_count = 0

    if left:
        win.blit(Left_walking[walk_count // 3], (char_x, char_y))
        walk_count += 1
    elif right:
        win.blit(Right_walking[walk_count // 3], (char_x, char_y))
        walk_count += 1
    else:
        win.blit(char, (char_x, char_y))

    pygame.display.update()


while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and char_x > speed:
        char_x -= speed
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and char_x < 1330 - speed - width:
        char_x += speed
        right = True
        left = False
    else:
        left = False
        right = False
        walkCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            char_y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
    rock_movement()
    draw_game()
    game_over()
