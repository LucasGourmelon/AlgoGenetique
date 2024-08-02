import tkinter as tk

class Ant():
    def __init__(self, x, y, attack, speed, pv, stamina, images, angle=0):
        self.x = x
        self.y = y
        self.attack = attack
        self.speed = speed
        self.pv = pv
        self.stamina = stamina
        self.images = images
        self.indexCurrentImage = 0
        self.angle = angle

    def setXY(self, x, y):
        self.x = x
        self.y = y

    def nextImage(self):
        if self.indexCurrentImage == len(self.images) - 1:
            self.indexCurrentImage = 0
        else:
            self.indexCurrentImage = self.indexCurrentImage + 1
        
        return self.indexCurrentImage

    def __str__(self):
        return "Ant: {self.attack} {self.speed} {self.pv} {self.stamina}"


