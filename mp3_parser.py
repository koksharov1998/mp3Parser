import argparse

import pygame


def parse_args():
    parser = argparse.ArgumentParser(description='User database utility')


def main():
    play()


def play():
    pygame.init()
    pygame.display.set_caption('Player')
    player = pygame.display.set_mode((300, 100))
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.load('music.mp3')

    pygame.mixer.music.play()
    is_alive = True
    while is_alive:
        player.fill((255, 255, 255))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_alive = False
                continue
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
    main()
