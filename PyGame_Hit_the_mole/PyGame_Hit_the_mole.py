#!/usr/bin/python
# -*- encoding: utf-8 -*-


# ESA 2: PyGame: Hit the mole
__author__ = "Daniel Riel"
__version__ = "1.0"


# IDEA
# Import and Initialization
import pygame
import random
from pygame.locals import *
pygame.init()

SET_TIMER_ONOFF = 1  # 0 -> OFF, 1 -> ON

# Display configuration
# Window properties
SCREEN_WIDTH = 640
SCREEN_HEIGTH = 480

# Text properties
POS_X = 0
POS_Y = 0
update_points = 0
FONT_SIZE = 15
FONT_TYPE = "arial"
FONT_COLOR = (0, 0, 0)
counter, text = 3, '3'.rjust(3)

# Properties for holes
HOLE_COLOR = (153, 76, 0)
RADIUS = 20
new_posx = [random.randint(50, 600)]
new_posy = [random.randint(50, 400)]

# Icon properties
ICON_WIDTH = 40
ICON_HEIGTH = 40


pygame.display.set_caption('Pygame: Hit the mole')  # Set window title
custom_cursor = pygame.transform.scale(pygame.image.load(
    "icon\hammer.png"), (32, 32))  # Image for "custom" cursor
pygame.mouse.set_visible(False)  # Hide the OS cursor
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
text_font = pygame.font.SysFont(FONT_TYPE, FONT_SIZE)
soundfile_hit = pygame.mixer.music.load("soundfile\hit.mp3")  # Load sound file
mole_icon = pygame.image.load("icon\mole.png")  # Load image file
# mole_icon = pygame.transform.scale(mole_icon, (ICON_WIDTH, ICON_HEIGTH))
pygame.time.set_timer(pygame.USEREVENT, 1000)  # Timer/Counter speed


# Action --> ALTER
# Assign Variables
FPS_CLOCK = pygame.time.Clock()
run = True


def play_sound():
    '''Play sound'''
    # Start playing the sound file
    pygame.mixer.music.play()


def draw_text(text, text_font, FONT_COLOR, POS_X, POS_Y):
    '''Draw text points'''
    img_text_points = text_font.render(text, True, FONT_COLOR)
    screen.blit(img_text_points, (POS_X, POS_Y))


def update_game_points(update_points, text_font, FONT_COLOR, POS_Y):
    '''Draw game points'''
    img_update_text_points = text_font.render(
        "%d" % update_points, True, FONT_COLOR)
    screen.blit(img_update_text_points, (50, POS_Y))


def draw_mole():
    '''Draw mole'''
    # Draw the mole at a random position
    # rect = mole_icon.get_rect()
    # rect.center = new_posx[0], new_posy[0]
    # screen.blit(mole_icon, rect)
    pygame.draw.circle(screen, HOLE_COLOR, (new_posx[0], new_posy[0]), RADIUS)
    pygame.display.set_icon(mole_icon)


# Loop
while run:
    # Timer
    if SET_TIMER_ONOFF == 1:
        FPS_CLOCK.tick(30)

    screen.fill((240, 255, 255))
    draw_text("Points: ", text_font, FONT_COLOR, POS_X, POS_Y)
    update_game_points(update_points, text_font, FONT_COLOR, POS_Y)
    draw_mole()
    # Paint cursor at the current location
    screen.blit(custom_cursor, (pygame.mouse.get_pos()))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.USEREVENT:
            counter -= 1
            if counter > 0:
                text = str(counter).rjust(3)
            else:
                # Calculate new mole at x position (if timer equals 0)
                new_posx = [random.randint(50, 600)]
                # Calculate new mole at y position (if timer equals 0)
                new_posy = [random.randint(50, 400)]
                counter, text = 3, '3'.rjust(3)  # Timer reset
                if update_points != 0:
                    update_points -= 1  # No hit -> decrement score
                else:
                    update_points = 0  # No negative score
        # Handle mouse event
        # Left mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Mouse collition within a circle
            collide = screen.get_at(pygame.mouse.get_pos()) == HOLE_COLOR
            if collide == 1:
                update_points += 1  # Hit mole -> increment score
                play_sound()
                # Calculate new mole at x position
                new_posx = [random.randint(50, 600)]
                # Calculate new mole at y position
                new_posy = [random.randint(50, 400)]
                counter, text = 3, '3'.rjust(3)  # Timer reset

    screen.blit(text_font.render(text, True, FONT_COLOR),
                (SCREEN_WIDTH-30, SCREEN_HEIGTH-20))  # Render text to screen window
    pygame.display.update()

pygame.quit()