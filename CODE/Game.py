import pygame
import os
from CODE.Car import Car
from CODE.Enemy import Enemy
from CODE.Bomb import Bomb
from CODE.Bullet import Bullet
from CODE.music import play_next_song

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 0)
BLUE = (0, 0, 255)
size = (1020, 620)


class Game:
    def go(lives, level, carryOn, playlist, IMAGES_Folder, MUSIC_Folder, enemyCarExists, enemyCarBouncerExists):
        pygame.init()
        screen = pygame.display.set_mode(size)
        if level == 1:
            filename = "scafell.jpeg"
            levelsincluded = "1"
        if level == 2:
            filename = "collage.jpg"
            levelsincluded = "12"
        if level == 3:
            filename = "newyorkbeach2.jpeg"
            levelsincluded = "3"
        if level == 4:
            filename = "japan.png"
            levelsincluded = "1"
        if level == 5:
            filename = "justgo.png"
            levelsincluded = "12"
        if level == 6:
            filename = "tunisia.png"
            levelsincluded = "3"
        if level == 7:
            filename = "badminton.jpeg"
        os.chdir(IMAGES_Folder)
        backgroundImage = pygame.image.load(filename).convert()
        backgroundImage = pygame.transform.scale(backgroundImage, (1020, 620))
        pygame.display.set_caption("***** SPACE INVADERS *****")
        clock = pygame.time.Clock()
        all_sprites_list = pygame.sprite.Group()
        os.chdir(MUSIC_Folder)
        shootSound = pygame.mixer.Sound('laser.wav')
        shootSound.set_volume(0.10)
        bombSound = pygame.mixer.Sound('falling.wav')
        bombSound.set_volume(0.10)
        applauseSound = pygame.mixer.Sound('applause.wav')
        playerCar = Car(RED, 40, 10)
        playerCar.rect.x = 510
        playerCar.rect.y = 580
        life = []
        for x in range(0, lives):
            life.append(Car(RED, 40, 10))
            life[x].rect.x = 0
            life[x].rect.y = x * 20
        if "1" in levelsincluded:
            if enemyCarExists:
                enemyCar = Enemy(GREEN, 40, 10)
                enemyCar.rect.x = 100
                enemyCar.rect.y = 100
                all_sprites_list.add(enemyCar)
                enemyBomb = []
                enemyBomb.append(Bomb(GREEN, 10, 10))
                enemyBomb[0].rect.x = 100
                enemyBomb[0].rect.y = 100
                bombSound.play()
                all_sprites_list.add(enemyBomb[0])
        if "2" in levelsincluded:
            if enemyCarBouncerExists:
                enemyCarBouncer = Enemy(PURPLE, 20, 20)
                enemyCarBouncer.rect.x = 500
                enemyCarBouncer.rect.y = 200
                all_sprites_list.add(enemyCarBouncer)
                enemyBouncerBomb = []
                enemyBouncerBomb.append(Bomb(PURPLE, 10, 10))
                enemyBouncerBomb[0].rect.x = 100
                enemyBouncerBomb[0].rect.y = 100
                all_sprites_list.add(enemyBouncerBomb)
        if "3" in levelsincluded:
            enemyTeamCar = []
            for x in range(0, 5):
                enemyTeamCar.append(Enemy(BLUE, 20, 10))
                enemyTeamCar[x].rect.x = 100 * (x + 1)
                enemyTeamCar[x].rect.y = 50
            for x in range(5, 10):
                enemyTeamCar.append(Enemy(BLUE, 20, 10))
                enemyTeamCar[x].rect.x = 100 * (x - 4)
                enemyTeamCar[x].rect.y = 100
            all_sprites_list.add(enemyTeamCar)
            protectionWalls = []
            for x in range(0, 9):
                protectionWalls.append(Car(BLACK, 40, 10))
                protectionWalls[x].rect.x = 95 * (x + 1)
                protectionWalls[x].rect.y = 500
            all_sprites_list.add(protectionWalls)
        playerBullet = []
        all_sprites_list.add(playerCar)
        all_sprites_list.add(life)
        while carryOn:
            if enemyCarExists:
                for x in range(0, enemyBomb.__len__()):
                    enemyBomb[x].rect.y = enemyBomb[x].rect.y + 10
                    hitByBomb = pygame.sprite.spritecollideany(playerCar, enemyBomb)
                    if hitByBomb:
                        playerCar.rect.x = 0
                        playerCar.rect.y = 0
                        enemyBomb[x].rect.x = 1000
                        enemyBomb[x].rect.y = 1000
                        playerBullet.clear()
                        enemyBomb.clear()
                        basicfont = pygame.font.SysFont("comicsansms", 72)
                        text = basicfont.render('XXX YOU LOST A LIFE XXX', True, BLACK, WHITE)
                        textrect = text.get_rect()
                        textrect.centerx = screen.get_rect().centerx
                        textrect.centery = screen.get_rect().centery
                        screen.blit(text, textrect)
                        pygame.display.flip()
                        pygame.time.delay(5000)
                        return lives - 1, level, carryOn, enemyCarExists, enemyCarBouncerExists
                    elif enemyBomb[x].rect.y > 580:
                        enemyBomb[x].rect.x = 1000
                        enemyBomb[x].rect.y = 1000
                        enemyBomb.pop(x)
                if enemyBomb.__len__() < 1:
                    enemyBomb.append(Bomb(GREEN, 10, 10))
                    enemyBomb[-1].rect.x = enemyCar.rect.x
                    enemyBomb[-1].rect.y = enemyCar.rect.y
                    bombSound.play()
                    all_sprites_list.add(enemyBomb[-1])
                if enemyCar.rect.x < 10:
                    enemyCar.direction = 'right'
                if enemyCar.rect.x > 970:
                    enemyCar.direction = 'left'
                if enemyCar.rect.x > 10 and enemyCar.direction == 'right':
                    enemyCar.moveRight(1, 5)
                elif enemyCar.rect.x > 10 and enemyCar.direction == 'left':
                    enemyCar.moveLeft(1, 5)
                elif enemyCar.rect.x < 970 and enemyCar.direction == 'left':
                    enemyCar.moveLeft(1, 5)
                elif enemyCar.rect.x < 970 and enemyCar.direction == 'right':
                    enemyCar.moveRight(1, 5)
            if "2" in levelsincluded:
                if enemyCarBouncerExists:
                    for x in range(0, enemyBouncerBomb.__len__()):
                        enemyBouncerBomb[x].rect.y = enemyBouncerBomb[x].rect.y + 10
                        hitByBouncerBomb = pygame.sprite.spritecollideany(playerCar, enemyBouncerBomb)
                        if hitByBouncerBomb:
                            playerCar.rect.x = 0
                            playerCar.rect.y = 0
                            enemyBouncerBomb[x].rect.x = 1000
                            enemyBouncerBomb[x].rect.y = 1000
                            playerBullet.clear()
                            enemyBouncerBomb.clear()
                            basicfont = pygame.font.SysFont("comicsansms", 72)
                            text = basicfont.render('XXX YOU LOST A LIFE XXX', True, BLACK, WHITE)
                            textrect = text.get_rect()
                            textrect.centerx = screen.get_rect().centerx
                            textrect.centery = screen.get_rect().centery
                            screen.blit(text, textrect)
                            pygame.display.flip()
                            pygame.time.delay(5000)
                            return lives - 1, level, carryOn, enemyCarExists, enemyCarBouncerExists
                        elif enemyBouncerBomb[x].rect.y > 580:
                            enemyBouncerBomb[x].rect.x = 1000
                            enemyBouncerBomb[x].rect.y = 1000
                            enemyBouncerBomb.pop(x)
                    if enemyBouncerBomb.__len__() < 1:
                        enemyBouncerBomb.append(Bomb(PURPLE, 10, 10))
                        enemyBouncerBomb[-1].rect.x = enemyCarBouncer.rect.x
                        enemyBouncerBomb[-1].rect.y = enemyCarBouncer.rect.y
                        all_sprites_list.add(enemyBouncerBomb[-1])
                    if enemyCarBouncer.rect.x < 10:
                        enemyCarBouncer.direction = 'right'
                    if enemyCarBouncer.rect.x > 970:
                        enemyCarBouncer.direction = 'left'
                    if enemyCarBouncer.rect.y < 10:
                        enemyCarBouncer.UDdirection = 'down'
                    if enemyCarBouncer.rect.y > 410:
                        enemyCarBouncer.UDdirection = 'up'
                    if enemyCarBouncer.rect.x > 10 and enemyCarBouncer.direction == 'right' and enemyCarBouncer.UDdirection == "up":
                        enemyCarBouncer.moveDiagRightUp()
                    elif enemyCarBouncer.rect.x > 10 and enemyCarBouncer.direction == 'right' and enemyCarBouncer.UDdirection == "down":
                        enemyCarBouncer.moveDiagRightDown()
                    elif enemyCarBouncer.rect.x > 10 and enemyCarBouncer.direction == 'left' and enemyCarBouncer.UDdirection == "up":
                        enemyCarBouncer.moveDiagLeftUp()
                    elif enemyCarBouncer.rect.x > 10 and enemyCarBouncer.direction == 'left' and enemyCarBouncer.UDdirection == "down":
                        enemyCarBouncer.moveDiagLeftDown()
                    elif enemyCarBouncer.rect.x < 970 and enemyCarBouncer.direction == 'right' and enemyCarBouncer.UDdirection == "up":
                        enemyCarBouncer.moveDiagRightUp()
                    elif enemyCarBouncer.rect.x < 970 and enemyCarBouncer.direction == 'right' and enemyCarBouncer.UDdirection == "down":
                        enemyCarBouncer.moveDiagRightDown()
                    elif enemyCarBouncer.rect.x < 970 and enemyCarBouncer.direction == 'left' and enemyCarBouncer.UDdirection == "up":
                        enemyCarBouncer.moveDiagLeftUp()
                    elif enemyCarBouncer.rect.x < 970 and enemyCarBouncer.direction == 'left' and enemyCarBouncer.UDdirection == "down":
                        enemyCarBouncer.moveDiagLeftDown()

            if "3" in levelsincluded:
                if enemyTeamCar[0].rect.x < 20:
                    enemyTeamCar[0].direction = 'right'
                    enemyTeamCar[4].direction = 'right'
                if enemyTeamCar[4].rect.x > 970:
                    enemyTeamCar[4].direction = 'left'
                    enemyTeamCar[0].direction = 'left'
                if enemyTeamCar[0].rect.x > 20 and enemyTeamCar[0].direction == 'right':
                    for z in range(0, 10):
                        enemyTeamCar[z].moveRight(1, 1)
                elif enemyTeamCar[0].rect.x > 20 and enemyTeamCar[0].direction == 'left':
                    for z in range(0, 10):
                        enemyTeamCar[z].moveLeft(1, 1)
                elif enemyTeamCar[4].rect.x < 970 and enemyTeamCar[4].direction == 'left':
                    for z in range(0, 10):
                        enemyTeamCar[z].moveLeft(1, 1)
                elif enemyTeamCar[4].rect.x < 970 and enemyTeamCar[4].direction == 'right':
                    for z in range(0, 10):
                        enemyTeamCar[z].moveRight(1, 1)

            for x in range(0, playerBullet.__len__()):
                if enemyCarExists:
                    hitByBullet = pygame.sprite.spritecollideany(enemyCar, playerBullet)
                    if hitByBullet:
                        enemyCar.rect.x = 1000
                        enemyCar.rect.y = 1000
                        for d in range(0, playerBullet.__len__()):
                            playerBullet[d].rect.x = 1000
                            playerBullet[d].rect.y = 1000
                        playerBullet.clear()
                        for d in range(0, enemyBomb.__len__()):
                            enemyBomb[d].rect.x = 1000
                            enemyBomb[d].rect.y = 1000
                        enemyBomb.clear()
                        if level == 1:
                            applauseSound.play()
                            basicfont = pygame.font.SysFont("comicsansms", 72)
                            text = basicfont.render('!!! LEVEL ' + str(level) + ' Completed !!!', True, BLACK, WHITE)
                            textrect = text.get_rect()
                            textrect.centerx = screen.get_rect().centerx
                            textrect.centery = screen.get_rect().centery
                            screen.blit(text, textrect)
                            pygame.display.flip()
                            pygame.time.delay(5000)
                            return lives, level + 1, carryOn, enemyCarExists, enemyCarBouncerExists
                        if level == 2:
                            enemyCarExists = False
                            if enemyCarBouncerExists == False:
                                applauseSound.play()
                                basicfont = pygame.font.SysFont("comicsansms", 72)
                                text = basicfont.render('!!! LEVEL ' + str(level) + ' Completed !!!', True, BLACK, WHITE)
                                textrect = text.get_rect()
                                textrect.centerx = screen.get_rect().centerx
                                textrect.centery = screen.get_rect().centery
                                screen.blit(text, textrect)
                                pygame.display.flip()
                                pygame.time.delay(5000)
                                return lives, level + 1, carryOn, enemyCarExists, enemyCarBouncerExists
                            break
                if "2" in levelsincluded:
                    if enemyCarBouncerExists:
                        hitByBullet = pygame.sprite.spritecollideany(enemyCarBouncer, playerBullet)
                        if hitByBullet:
                            enemyCarBouncer.rect.x = 1000
                            enemyCarBouncer.rect.y = 1000
                            for d in range(0, playerBullet.__len__()):
                                playerBullet[d].rect.x = 1000
                                playerBullet[d].rect.y = 1000
                            playerBullet.clear()
                            for d in range(0, enemyBouncerBomb.__len__()):
                                enemyBouncerBomb[d].rect.x = 1000
                                enemyBouncerBomb[d].rect.y = 1000
                            enemyBouncerBomb.clear()
                            if enemyCarExists:
                                for d in range(0, enemyBomb.__len__()):
                                    enemyBomb[d].rect.x = 1000
                                    enemyBomb[d].rect.y = 1000
                                    enemyBomb.clear()
                            if level == 2 and enemyCarExists == False:
                                applauseSound.play()
                                basicfont = pygame.font.SysFont("comicsansms", 72)
                                text = basicfont.render('!!! LEVEL ' + str(level) + ' Completed !!!', True, BLACK, WHITE)
                                textrect = text.get_rect()
                                textrect.centerx = screen.get_rect().centerx
                                textrect.centery = screen.get_rect().centery
                                screen.blit(text, textrect)
                                pygame.display.flip()
                                pygame.time.delay(5000)
                                enemyCarBouncerExists = False
                                return lives, level + 1, carryOn, enemyCarExists, enemyCarBouncerExists
                            if level == 2:
                                enemyCarBouncerExists = False
                                if enemyCarExists == False:
                                    applauseSound.play()
                                    basicfont = pygame.font.SysFont("comicsansms", 72)
                                    text = basicfont.render('!!! LEVEL ' + str(level) + ' Completed !!!', True, BLACK, WHITE)
                                    textrect = text.get_rect()
                                    textrect.centerx = screen.get_rect().centerx
                                    textrect.centery = screen.get_rect().centery
                                    screen.blit(text, textrect)
                                    pygame.display.flip()
                                    pygame.time.delay(5000)
                                    return lives, level + 1, carryOn, enemyCarExists, enemyCarBouncerExists
                                break

                if "3" in levelsincluded:
                    hitByBullet = pygame.sprite.groupcollide(playerBullet, enemyTeamCar, False, False)
                    if hitByBullet:
                        print(hitByBullet.items())

                if playerBullet[x].rect.y < 11:
                    playerBullet[x].rect.x = 1000
                    playerBullet[x].rect.y = 1000
                    playerBullet.pop(x)
                    break

                if playerBullet[x].rect.y > 10:
                    playerBullet[x].rect.y = playerBullet[x].rect.y - 10

            for event in pygame.event.get():  # User did something
                SONG_END = pygame.USEREVENT + 1
                if event.type == SONG_END:
                    os.chdir(MUSIC_Folder)
                    play_next_song(playlist)
                if event.type == pygame.QUIT:
                    carryOn = False
                    return lives, level, carryOn, enemyCarExists, enemyCarBouncerExists

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        carryOn = False
                        return lives, level, carryOn, enemyCarExists, enemyCarBouncerExists

                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_o]:
                        if playerCar.rect.x > 10:
                            playerCar.moveLeft(10)
                    if keys[pygame.K_p]:
                        if playerCar.rect.x < 970:
                            playerCar.moveRight(10)
                    if keys[pygame.K_q] and playerBullet.__len__() < 2:
                        playerBullet.append(Bullet(RED, 2, 2))
                        playerBullet[-1].rect.x = playerCar.rect.x + 19
                        playerBullet[-1].rect.y = playerCar.rect.y
                        shootSound.play()
                        all_sprites_list.add(playerBullet[-1])

            # --- Game logic should go here

            all_sprites_list.update()
            # --- Drawing code should go here
            screen.fill(WHITE)
            screen.blit(backgroundImage, [0, 0])
            all_sprites_list.draw(screen)
            pygame.display.flip()
            clock.tick(60)
