import pygame


def play_next_song(playlist):
    playlist = playlist[1:] + [playlist[0]]
    pygame.mixer.music.load(playlist[0])
    pygame.mixer.music.play()
