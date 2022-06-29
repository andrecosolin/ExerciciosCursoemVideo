# ex021
# Faça um programa em python que abre e reproduza o áudio de um arquivo MP3

print('='*11,'ex021','='*11)

# import webbrowser
#
# musica = str(input('Escreva música para tocar: '))
# webbrowser.open('https://www.suamusica.com.br/ElMagroDJ/acdc-back-in-black')
# print('Clique em play para ouvir a música!')

# from playsound import playsound
# playsound('/home/andre-martins/PycharmProjects/acdc.mp3')

import pygame
pygame.init()
pygame.mixer.music.load('ex021acdc.mp3')
pygame.mixer.music.play()
pygame.event.wait()