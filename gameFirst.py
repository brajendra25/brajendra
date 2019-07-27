import pygame
pygame.init()

window_w = 600
window_h = 400

white = (255, 255, 255)
black = (0, 0, 0)

FPS = 120

window = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption("Game: Brajendra Shukla")
clock = pygame.time.Clock()

def game_loop():
    block_size = 20
    velocity = [1, 1]
    pos_x = window_w/2
    pos_y = window_h/2
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pos_x += velocity[0]
        pos_y += velocity[1]

        if pos_x + block_size > window_w or pos_x < 0:
            velocity[0] = -velocity[0]

        if pos_y + block_size > window_h or pos_y < 0:
            velocity[1] = -velocity[1]

        # DRAW
        window.fill(black)
        pygame.draw.rect(window, white, [pos_x, pos_y, block_size, block_size])
        blue = 0, 0, 255
        point1 = pos_x, pos_y
        point2 = 250, 200
        pygame.draw.line(window, blue, point1, point2)       
        pygame.display.update()
        clock.tick(FPS)


game_loop()