import random

import pygame
from pygame.math import Vector2
import core
import creep


class Avatar:
    def __init__(self,largeur=400,hauteur=400):
        self.position = Vector2(400,400)
        self.taille = 10
        self.tailleMAX = 100
        self.couleur = (255,0,0)
        self.masse = 10
        self.vel = Vector2(0,0)
        self.maxAcc = 300
        self.maxVel = 440
        self.count = 0


    def deplacement(self, destination):
        print(destination)

        if destination is not None:
            #bilan des force

            self.vel=destination -self.position
            self.vel = self.vel.normalize()

        #limiter la vitesse si trop grande
        if self.vel.length() > self.maxVel:
            self.vel.scale_to_length(self.maxVel)

        #ajouter vitesse a position
        self.position += self.vel

        #distance ?
        #distance - r1-r2 <0


    def eat(self,creep):
        if creep.position.distance_to(self.position) < creep.taille+ self.taille:
            creep.RAZ()
            self.taille= self.taille+ creep.taille

        elif self.taille > self.tailleMAX:
            self.taille= self.tailleMAX


    def show(self, screen):
        pygame.draw.circle(screen,self.couleur,self.position,self.taille)

    def bord(self, screen):
        if self.position[0] > core.WINDOW_SIZE[0]:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = core.WINDOW_SIZE[0]
        elif self.position[1] > core.WINDOW_SIZE[1]:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = core.WINDOW_SIZE[1]
