class Ant:
    def __init__(self, x, y, attack, speed, pv, stamina, range, angle=0):
        self.x = x
        self.y = y
        self.attack = attack
        self.speed = speed
        self.pv = pv
        self.stamina = stamina
        self.angle = angle
        self.isMoving = False
        self.range = range
        self.history = []
        self.targetQueue = []
        
        self.score = 0

    def setXY(self, x, y):
        self.x = x
        self.y = y

    def stopMovement(self):
        self.isMoving = False
        self.targetQueue.clear()