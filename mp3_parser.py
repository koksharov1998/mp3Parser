import argparse

import pygame


def parse_args():
    parser = argparse.ArgumentParser(description='User database utility')


def temp():
    f = open('music2.mp3', 'rb')
    f.seek(30000000, 2)
    print(f.read(20))


def main():
    f = open('music2.mp3', 'rb')
    three = "###"
    i = 5
    for b in f.read(140).decode(encoding='utf-8'):
        print(three)
        three = three[1] + three[2] + b
        # i -= 1
        # if i < 0:
        #   break
    # print(f.read(142).decode(encoding='utf-8'))
    # print(f.read(24).decode(encoding='utf-8'))
    # print(f.read(100).decode(encoding='utf-8'))
    f.close()
    # play()


def play():
    pygame.init()
    pygame.display.set_caption('Player')
    player = pygame.display.set_mode((300, 100))

    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.load('music1.mp3')
    pygame.mixer.music.play()

    circle_color = (0, 0, 255)
    circle_pos = (50, 50)
    circle_radius = 10
    circle_width = 0
    pygame.draw.circle(player, circle_color, circle_pos, circle_radius, circle_width)

    is_alive = True
    while is_alive:
        player.fill((255, 255, 255))
        pause = pygame.draw.circle(player, circle_color, circle_pos, circle_radius, circle_width)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_alive = False
                continue
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pause.collidepoint(event.pos):
                    pygame.mixer.music.pause()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    pygame.mixer.music.unpause()
                elif event.key == pygame.K_s:
                    pygame.mixer.music.pause()
                elif event.key == pygame.K_d:
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.05)
                    print(pygame.mixer.music.get_volume())
                elif event.key == pygame.K_a:
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.05)
                    print(pygame.mixer.music.get_volume())

    pygame.mixer.quit()
    pygame.quit()


if __name__ == '__main__':
    temp()
    # main()
