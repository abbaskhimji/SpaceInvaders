import pygame
import os
from CODE.Game import Game
pygame.init()
lives = 3
level = 1
playlist = list()
playlist.append('Galvanize.mp3')
playlist.append('Cruel Summer.mp3')
playlist.append('now your gone.mp3')
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
print(os.getcwd())
APP_Folder = os.getcwd()
CODE_Folder = str(os.getcwd()) + '/CODE/'
MUSIC_Folder = str(os.getcwd()) + '/MUSIC/'
IMAGES_Folder = str(os.getcwd()) + '/IMAGES/'
os.chdir(MUSIC_Folder)
pygame.mixer.music.load('Eye Of The Tiger.mp3')
pygame.mixer.music.play()
carryOn = True
enemyCar = True
enemyBouncerCar = True
while level < 4 and lives > -2 and carryOn:
    if lives == -1:
        print("game over")
        break
    elif level == 1:
        lives, level, carryOn, enemyCar, enemyBouncerCar = Game.go(lives, level, carryOn, playlist, IMAGES_Folder, MUSIC_Folder, enemyCar, enemyBouncerCar)
    elif level == 2:
        lives, level, carryOn, enemyCar, enemyBouncerCar = Game.go(lives, level, carryOn, playlist, IMAGES_Folder, MUSIC_Folder, enemyCar, enemyBouncerCar)
    elif level == 3:
        lives, level, carryOn, enemyCar, enemyBouncerCar = Game.go(lives, level, carryOn, playlist, IMAGES_Folder, MUSIC_Folder, enemyCar, enemyBouncerCar)
    if level == 4:
        print("well done you completed the game")
        break
    if carryOn == False:
        print("quit game")
        break
pygame.quit()
