import constants

from random import randint

from Ant import Ant


class AntManager:
    @staticmethod
    def generate_random_ant():
        x = randint(0, constants.WINDOW_WIDTH)
        y = randint(0, constants.WINDOW_HEIGHT)
        attack = randint(0, 100)
        defense = randint(0, 100)
        speed = randint(0, 100)
        stamina = randint(0, 100)

        max_range = min(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT) // 5
        radius = randint(10, max_range)

        history_size = randint(1, 100)

        depth = randint(1, 100)

        return Ant(x, y, attack, defense, speed, stamina, radius, history_size, depth)