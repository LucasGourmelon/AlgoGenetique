import constants

from random import randint
import math


class Ant:
    def __init__(self, x, y, attack, speed, pv, stamina, radius, history_size, depth=10):
        self.x = x
        self.y = y
        self.attack = attack
        self.speed = speed
        self.pv = pv
        self.stamina = stamina
        self.angle = 0
        self.isMoving = False
        self.radius = radius
        self.historySize = history_size
        self.depth = depth
        self.history = []
        self.targetQueue = []
        self.targetQueueIndex = 0
        self.score = 0

    @staticmethod
    def distance(point1, point2):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def get_xy(self):
        return self.x, self.y

    def stop_movement(self):
        self.isMoving = False
        self.targetQueue.clear()

    def add_history(self, x, y):
        self.history.append((x, y))
        if len(self.history) > self.historySize:
            self.history.pop(0)

    def is_in_history(self, point):
        return point in self.history

    def  check_food_in_radius(self, foods):
        for food in foods:
            distance = math.sqrt((food[0] - self.x) ** 2 + (food[1] - self.y) ** 2)
            if distance <= self.radius:
                return food
        return None

    def generate_points(self):
        points = []
        max_attempts = 10

        def is_too_close(point, new_point):
            return (point[0] - new_point[0]) ** 2 + (point[1] - new_point[1]) ** 2 <= (self.radius * 1.5) ** 2

        for _ in range(self.depth):
            attempts = 0
            while attempts < max_attempts:
                new_point = (randint(10, constants.WINDOW_WIDTH - 10), randint(10, constants.WINDOW_HEIGHT - 10))
                if not any(is_too_close(p, new_point) for p in self.history + points):
                    points.append(new_point)
                    break
                attempts += 1
        return points

    def get_next_point(self, last_point, remaining_points):
        if not remaining_points:
            return None

        closest_point = min(remaining_points, key=lambda p: self.distance(last_point, p))

        if self.distance(last_point, closest_point) <= self.radius:
            remaining_points.remove(closest_point)
            return closest_point
        else:
            return closest_point

    def find_optimal_path(self):
        points = self.generate_points()
        path = [(self.x, self.y)]
        remaining_points = set(points)
        stuck_counter = 0

        while remaining_points:
            last_point = path[-1]
            next_point = self.get_next_point(last_point, remaining_points)

            if next_point is None:
                break

            if next_point in path:
                stuck_counter += 1
            else:
                stuck_counter = 0

            if stuck_counter > self.depth // 2:
                remaining_points = set(self.generate_points())
                stuck_counter = 0

            path.append(next_point)
            if next_point in remaining_points:
                remaining_points.remove(next_point)

        return path

    def to_string(self):
        return f"Ant: x={self.x}, y={self.y}, attack={self.attack}, speed={self.speed}, pv={self.pv}, stamina={self.stamina}, radius={self.radius}, historySize={self.historySize}, depth={self.depth}, score={self.score}"
