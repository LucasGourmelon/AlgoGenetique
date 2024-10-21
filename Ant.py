from random import randint
import math

class Ant:
    def __init__(self, x, y, attack, speed, pv, stamina, range, historySize, traceFrequency, angle=0):
        self.x = x
        self.y = y
        self.attack = attack
        self.speed = speed
        self.pv = pv
        self.stamina = stamina
        self.angle = angle
        self.isMoving = False
        self.range = range
        self.historySize = historySize
        self.traceFrequency = traceFrequency
        self.history = []
        self.targetQueue = []
        self.score = 0

    def setXY(self, x, y):
        self.x = x
        self.y = y

    def stopMovement(self):
        self.isMoving = False
        self.targetQueue.clear()
        
    def addHistory(self, x, y):
        self.history.append((x, y))
        if len(self.history) > self.historySize:
            self.history.pop(0)

    def getNewTarget(self, width, height):
        # Générer une première cible aléatoire
        newTarget = (randint(10, width - 10), randint(10, height - 10))
        
        iterations = 0
        max_iterations = 100  # Limiter les itérations
        
        # Comparer les carrés des distances au lieu de calculer la racine
        def is_too_close(point):
            return (point[0] - newTarget[0]) ** 2 + (point[1] - newTarget[1]) ** 2 <= (self.range * 2) ** 2
        
        # Boucle pour chercher une cible éloignée
        while any(is_too_close(point) for point in self.history):
            newTarget = (randint(10, width - 10), randint(10, height - 10))
            iterations += 1
            if iterations > max_iterations:
                break  # Limiter la recherche si trop d'itérations
        
        return newTarget