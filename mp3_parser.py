import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='User database utility')
    #parser.add_argument('-1', '--one', help='This will be option One')
    parser.add_argument('-n', '--name', nargs='?', help='This will be show name of test audio')
    parser.add_argument('-p', '--play', nargs='?', help='Run music file')
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.name:
        get_name(namespace.name)
    elif namespace.play:
        play(namespace.play)




def main():
    pass


def get_name(file):
    f = open('musics/' + file, 'rb')
    three = "###"
    i = 5
    flag = False
    string = ''
    for b in f.read(140).decode(encoding='utf-8'):
        if three == 'TIT' and not flag:
            #print(three)
            flag = True
        if not flag:
            three = three[1] + three[2] + b
        else:
            string = string + b
    print(string[8: string.find('T', 9)])
    # i -= 1
    # if i < 0:
    #   break
    # print(f.read(142).decode(encoding='utf-8'))
    # print(f.read(24).decode(encoding='utf-8'))
    # print(f.read(100).decode(encoding='utf-8'))
    f.close()
    # play()


def play(file):
    import pygame
    pygame.init()
    pygame.display.set_caption('Player')
    player = pygame.display.set_mode((300, 100))

    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.load('musics/' + file)
    pygame.mixer.music.play()

    circle_color = (0, 0, 255)
    circle_pos = (50, 50)
    circle_radius = 10
    circle_width = 0
    pygame.draw.circle(player, circle_color, circle_pos, circle_radius, circle_width)

    is_alive = True
    playing = True
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
                    if playing:
                        pygame.mixer.music.pause()
                        playing = False
                    else:
                        pygame.mixer.music.unpause()
                        playing = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    pygame.mixer.music.unpause()
                    playing = True
                elif event.key == pygame.K_s:
                    pygame.mixer.music.pause()
                    playing = False
                elif event.key == pygame.K_d:
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.05)
                    print(pygame.mixer.music.get_volume())
                elif event.key == pygame.K_a:
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.05)
                    print(pygame.mixer.music.get_volume())

    pygame.mixer.quit()
    pygame.quit()


if __name__ == '__main__':
    # play('music3.mp3')
    parse_args()
    #get_name()
    # main()
