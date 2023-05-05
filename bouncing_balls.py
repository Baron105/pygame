import pygame
import random
import math

BLACK = (0, 0, 0)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BALL_SIZE = 10

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0

def make_ball():
    ball = Ball()
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
    ball.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    ball.change_x = random.randrange(1 , 5)*random.choice([-1,1])
    ball.change_y = random.randrange(1 , 5)*random.choice([-1,1])

    return ball

def main():
    pygame.init()

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Bouncing Balls")
    font = pygame.font.Font(None, 25)
    done = False
    start_time = pygame.time.get_ticks()
    collision_count = 0
    ball_collision_count = 0
    clock = pygame.time.Clock()

    ball_list = []

    ball = make_ball()
    ball_list.append(ball)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    ball = make_ball()
                    ball_list.append(ball)

        for i, ball in enumerate(ball_list):
            ball.x += ball.change_x
            ball.y += ball.change_y

            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
                collision_count += 1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1
                collision_count += 1
                
            for other_ball in ball_list[i+1:]:
                dx = ball.x - other_ball.x
                dy = ball.y - other_ball.y
                distance = math.sqrt(dx*dx + dy*dy)
                if distance < BALL_SIZE * 2:
                    ball_collision_count += 1
                    angle = math.atan2(dy, dx)
                    mag1 = math.sqrt(ball.change_x*ball.change_x + ball.change_y*ball.change_y)
                    mag2 = math.sqrt(other_ball.change_x*other_ball.change_x + other_ball.change_y*other_ball.change_y)
                    dir1 = math.atan2(ball.change_y, ball.change_x)
                    dir2 = math.atan2(other_ball.change_y, other_ball.change_x)

                    final_xspeed_2 = mag1 * math.cos(dir1 - angle)
                    final_yspeed_2 = mag1 * math.sin(dir1 - angle)
                    final_xspeed_1 = mag2 * math.cos(dir2 - angle)
                    final_yspeed_1 = mag2 * math.sin(dir2 - angle)

                    ball.change_x = final_xspeed_1 * math.cos(angle) + final_yspeed_1 * math.cos(angle + math.pi/2)
                    ball.change_y = final_xspeed_1 * math.sin(angle) + final_yspeed_1 * math.sin(angle + math.pi/2)
                    other_ball.change_x = final_xspeed_2 * math.cos(angle) + final_yspeed_2 * math.cos(angle + math.pi/2)
                    other_ball.change_y = final_xspeed_2 * math.sin(angle) + final_yspeed_2 * math.sin(angle + math.pi/2)


        screen.fill(BLACK)

        for ball in ball_list:
            pygame.draw.circle(screen, ball.color, [ball.x, ball.y], BALL_SIZE)

        elapsed_time = pygame.time.get_ticks() - start_time
        ball_count = len(ball_list)

        ball_count_text = font.render("Balls: {}".format(ball_count), True, (255, 255, 255))
        elapsed_time_text = font.render("Elapsed Time: {:.2f} seconds".format(elapsed_time/1000), True, (255, 255, 255))
        collision_count_text = font.render("Wall Collisions: {}".format(collision_count), True, (255, 255, 255))
        ball_collision_count_text = font.render("Ball Collisions: {}".format(ball_collision_count), True, (255, 255, 255))
        screen.blit(ball_count_text, [10, 10])
        screen.blit(elapsed_time_text, [10, 30])
        screen.blit(collision_count_text, [10, 50])
        screen.blit(ball_collision_count_text, [10, 70])
        clock.tick(60)

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
