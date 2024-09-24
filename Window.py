import math
import tkinter as tk
from PIL import Image, ImageTk 
from Ant import Ant

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Algorithme génétique')
        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack()

        self.antImages = [
            Image.open("./imgs/ant1.png").resize((50, 50)), 
            Image.open("./imgs/ant2.png").resize((50, 50)),
            Image.open("./imgs/ant3.png").resize((50, 50))
        ]

        self.ant = Ant(100, 100, 0, 0, 0, 0, self.antImages)
        self.ant2 = Ant(200, 300, 0, 0, 0, 0, self.antImages)

        idImage = self.showAnt(self.ant)
        idImage2 = self.showAnt(self.ant2)
        
        self.animateAnt(self.ant, idImage)
        # self.animateAnt(self.ant2, idImage2)
        
        # self.moveAnt(self.ant, idImage, 300, 100)
        # self.moveAnt(self.ant, idImage, 500, 500)
        # self.moveAnt(self.ant, idImage, 500, 10)
        
        # self.moveAnt(self.ant2, idImage, 100, 10)
        # self.moveAnt(self.ant2, idImage, 500, 101)
        # self.moveAnt(self.ant2, idImage, 200, 310)
        
    def showAnt(self, ant):
        print(ant)
        antImage = ImageTk.PhotoImage(self.antImages[ant.indexCurrentImage].rotate(ant.angle))
        idImage = self.canvas.create_image(ant.x, ant.y, image=antImage)
        
        if not hasattr(self, 'antImagesReferences'):
            self.antImagesReferences = []
        self.antImagesReferences.append(antImage)
        
        return idImage

    def animateAnt(self, ant, idImage):
        ant.nextImage()
        antImage = ImageTk.PhotoImage(self.antImages[ant.indexCurrentImage].rotate(ant.angle))
        self.canvas.itemconfig(idImage, image=antImage)
        self.canvas.image = antImage  
        self.after(100, self.animateAnt, ant, idImage)

    def moveAnt(self, ant, idImageAnt, targetX, targetY, stopPrevious=False):
        if stopPrevious:
            ant.isMoving = False
            ant.targetQueue.clear()

        if ant.isMoving:
            ant.targetQueue.append((targetX, targetY))
            return

        ant.isMoving = True

        def update_position():
            nonlocal targetX, targetY, ant, idImageAnt

            differenceX = targetX - ant.x
            differenceY = targetY - ant.y
            # coeffDiff = 1 if differenceY == 0 else 1 - (differenceX / differenceY)

            # Calculer l'angle
            angle = math.degrees(math.atan2(differenceX,differenceY)) - 180
            ant.angle = angle

            # Mettre à jour l'image de la fourmi avec le nouvel angle
            antImage = ImageTk.PhotoImage(self.antImages[ant.indexCurrentImage].rotate(ant.angle))
            self.canvas.itemconfig(idImageAnt, image=antImage)
            self.canvas.image = antImage

            # Distance entre la fourmi et la cible
            distance = math.sqrt(differenceX ** 2 + differenceY ** 2)

            # Déplacement proportionnel à la distance, ici avec un pas fixe
            step_size = 2  # Ajuster la vitesse ici
            if distance > step_size:
                ant.x += (differenceX / distance) * step_size
                ant.y += (differenceY / distance) * step_size
            else:
                ant.x, ant.y = targetX, targetY  # La fourmi a atteint la cible

            # Mettre à jour la position de la fourmi sur le canvas
            self.canvas.coords(idImageAnt, ant.x, ant.y)

            # Vérifier si la fourmi a atteint la cible
            if abs(ant.x - targetX) < 1 and abs(ant.y - targetY) < 1:
                ant.isMoving = False  # La fourmi a atteint la cible
                if ant.targetQueue:
                    nextTarget = ant.targetQueue.pop(0)
                    self.moveAnt(ant, idImageAnt, nextTarget[0], nextTarget[1])
            else:
                self.after(10, update_position)  # Reprogrammer pour continuer le mouvement

        update_position()

if __name__ == "__main__":
    w = Window()
    w.mainloop()