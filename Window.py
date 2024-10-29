import constants

import tkinter as tk
from random import randint
import math

from Ant import Ant
from AntDisplay import AntDisplay
from AntManager import AntManager


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Algorithme génétique')
        self.canvas = tk.Canvas(self, width=constants.WINDOW_WIDTH, height=constants.WINDOW_HEIGHT)
        self.canvas.pack()
        self.foods = []
        self.ant = AntManager.generate_random_ant()
        print(self.ant.to_string())

        # self.ant = Ant(400, 400, 0, 0, 0, 0, 100, 10, 100)
        self.antDisplay = AntDisplay(self.canvas, self.ant)

        # self.generate_food()
        # self.animate_ant()
        # self.start_ant()

    def animate_ant(self):
        self.antDisplay.next_image()
        self.antDisplay.update_position()
        self.after(100, self.animate_ant)

    def start_ant(self):
        food = self.ant.check_food_in_radius(self.foods)

        if food:
            if math.sqrt((food[0] - self.ant.x) ** 2 + (food[1] - self.ant.y) ** 2) <= 10:
                self.remove_food(food)
                self.ant.score += 1
                self.generate_food()
            new_target = (food[0], food[1])
        else:
            target_queue = self.ant.find_optimal_path()
            self.ant.targetQueue = target_queue
            new_target = target_queue[0]

        self.move_ant(new_target[0], new_target[1])

    def move_ant(self, target_x_param, target_y_param):
        target_x, target_y = target_x_param, target_y_param

        if self.ant.isMoving:
            return
            return

        self.ant.isMoving = True

        def update_position():
            food = self.ant.check_food_in_radius(self.foods)

            if food:
                target_x, target_y = food[0], food[1]
            else:
                target_x, target_y = target_x_param, target_y_param

            self.canvas.delete("food")
            for i in range(len(self.ant.history)):
                x, y = self.ant.history[i]
                radiusFood = 5
                self.canvas.create_oval(x - radiusFood, y - radiusFood, x + radiusFood, y + radiusFood, fill='red',
                                        tags="food")

            differenceX = target_x - self.ant.x
            differenceY = target_y - self.ant.y
            distance = math.sqrt(differenceX ** 2 + differenceY ** 2)

            if distance > 2:
                self.ant.x += (differenceX / distance) * 2
                self.ant.y += (differenceY / distance) * 2
                self.ant.angle = math.degrees(math.atan2(differenceX, differenceY)) - 180
                self.antDisplay.update_image_angle()
                self.antDisplay.update_position()
                self.after(10, update_position)  # Continue la mise à jour de la position
            else:
                self.ant.x, self.ant.y = target_x, target_y
                self.ant.isMoving = False
                self.ant.add_history(target_x, target_y)

                if self.ant.targetQueue:
                    nextTarget = self.ant.targetQueue.pop(0)
                    self.move_ant(nextTarget[0], nextTarget[1])
                else:
                    self.start_ant()

        update_position()

    def generate_food(self):
        x, y = randint(0, constants.WINDOW_WIDTH), randint(0, constants.WINDOW_HEIGHT)
        foodId = self.canvas.create_oval(x - self.ant.radius / 2, y - self.ant.radius / 2, x + self.ant.radius / 2,
                                         y + self.ant.radius / 2, fill='yellow')
        self.canvas.tag_lower(foodId)

        self.foods.append((x, y, foodId))

        return x, y

    def remove_food(self, food):
        self.canvas.delete(food[2])
        self.foods.remove(food)


if __name__ == "__main__":
    w = Window()
    w.mainloop()
