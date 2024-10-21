import tkinter as tk 
from random import randint
import math

from Ant import Ant
from AntDisplay import AntDisplay

class Window(tk.Tk):
    WIDTH = 800
    HEIGHT = 600

    def __init__(self):
        super().__init__()
        self.title('Algorithme génétique')
        self.canvas = tk.Canvas(self, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()

        self.food = []
        self.ant = Ant(400, 400, 0, 0, 0, 0, 200, 10, 100)
        self.antDisplay = AntDisplay(self.canvas, self.ant)
                
        self.generateFood()
        self.animateAnt()
        self.startAnt()

    def animateAnt(self):
        self.antDisplay.nextImage()
        self.antDisplay.updatePosition()
        self.after(100, self.animateAnt)
        
    def checkFoodInRadius(self, radius):
        for food in self.food:
            distance = math.sqrt((food[0] - self.ant.x) ** 2 + (food[1] - self.ant.y) ** 2)
            if distance <= radius:
                return food
        return None

    def startAnt(self):
        food = self.checkFoodInRadius(self.ant.range) 
        if food:
            if math.sqrt((food[0] - self.ant.x) ** 2 + (food[1] - self.ant.y) ** 2) <= 10:        
                self.removeFood(food)            
                self.ant.score += 1
                self.generateFood()
            newTarget = (food[0], food[1])
        else:
            self.ant.targetQueue = []
            newTarget = self.ant.getNewTarget(self.WIDTH, self.HEIGHT)
                
        self.moveAnt(newTarget[0], newTarget[1])
        

    def moveAnt(self, targetXParam, targetYParam, stopMouvement = False):        
        targetX, targetY = targetXParam, targetYParam
        
        if self.ant.isMoving:
            self.ant.targetQueue.append((targetX, targetY))
            return

        self.ant.isMoving = True

        def update_position():
            food = self.checkFoodInRadius(self.ant.range)
            
            if food:
                targetX, targetY = food[0], food[1]
            else: 
                targetX, targetY = targetXParam, targetYParam
            
            if len(self.ant.history) == 0 or math.sqrt((self.ant.history[-1][0] - self.ant.x) ** 2 + (self.ant.history[-1][1] - self.ant.y) ** 2) > self.ant.range:
                self.ant.addHistory(self.ant.x, self.ant.y)
                x = self.ant.x
                y = self.ant.y
                
                self.canvas.delete("food")
                for i in range(len(self.ant.history)):
                    x, y = self.ant.history[i]
                    radiusFood = 5
                    self.canvas.create_oval(x - radiusFood, y - radiusFood, x + radiusFood, y + radiusFood, fill='red',tags="food")
            
            differenceX = targetX - self.ant.x
            differenceY = targetY - self.ant.y
            distance = math.sqrt(differenceX ** 2 + differenceY ** 2)

            if distance > 2:
                self.ant.x += (differenceX / distance) * 2
                self.ant.y += (differenceY / distance) * 2
            else:
                self.ant.x, self.ant.y = targetX, targetY
            
            self.ant.angle = math.degrees(math.atan2(differenceX, differenceY)) - 180
            self.antDisplay.updateImageAngle()
            self.antDisplay.updatePosition()

            if distance > 2:
                self.after(10, update_position)
            else:
                self.ant.isMoving = False
                if self.ant.targetQueue:
                    nextTarget = self.ant.targetQueue.pop(0)
                    self.moveAnt(nextTarget[0], nextTarget[1])
                else:
                    self.startAnt()

        update_position()

    def generateFood(self):
        x, y = randint(0, self.WIDTH), randint(0, self.HEIGHT)
        foodId = self.canvas.create_oval(x, y, x + 10, y + 10, fill='yellow')
        self.food.append((x, y, foodId))
        
        return x, y

    def removeFood(self, food):
        self.canvas.delete(food[2])
        self.food.remove(food)

if __name__ == "__main__":
    w = Window()
    w.mainloop()