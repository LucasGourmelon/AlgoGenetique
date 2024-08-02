import math
import tkinter as tk

from Ant import Ant

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Algorithme génétique')
        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack() 

        self.antImages = [
            tk.PhotoImage(file="./imgs/ant1.png").subsample(5,5),
            tk.PhotoImage(file="./imgs/ant2.png").subsample(5,5),
            tk.PhotoImage(file="./imgs/ant3.png").subsample(5,5)
        ]

        self.ant = Ant(0,0,0,0,0,0,self.antImages)

        idImage = self.showAnt(self.ant)
        self.animateAnt(self.ant,idImage)

        self.moveAnt(self.ant, idImage, 10, 10)

    def showAnt(self,ant): 
        antImage = self.antImages[ant.indexCurrentImage]
        idImage = self.canvas.create_image(ant.x, ant.y, image=antImage, anchor='nw')

        return idImage
    
    def animateAnt(self, ant, idImage): 
        ant.nextImage()
        antImage = self.antImages[ant.indexCurrentImage]
        self.canvas.itemconfig(idImage, image=antImage)
        self.after(200, self.animateAnt, ant, idImage)

    def moveAnt(self, ant, idImageAnt, targetX, targetY):
        # Mise à jour de la position de la fourmi
        if ant.x < targetX:
            ant.x += 1
        elif ant.x > targetX:
            ant.x -= 1

        if ant.y < targetY:
            ant.y += 1
        elif ant.y > targetY:
            ant.y -= 1

        # Calcul de l'angle actuel (supposons que vous ayez une variable ant.angle)
        current_angle = ant.angle 

        # Calcul de l'angle cible
        dx = targetX - ant.x
        dy = targetY - ant.y
        target_angle = math.atan2(dy, dx)  # L'angle est en radians

        # Convertir l'angle cible en degrés pour l'affichage
        target_angle_degrees = math.degrees(target_angle)

        # Mise à jour de l'angle de la fourmi
        ant.angle = target_angle_degrees

        # Appliquer la rotation sur le canvas
        # Par exemple, en utilisant la méthode canvas.itemconfig pour modifier l'angle
        self.canvas.itemconfig(idImageAnt, angle=ant.angle)

        # Déplacer l'image de la fourmi sur le canvas
        self.canvas.move(idImageAnt, ant.x, ant.y)

        # Appel récursif pour continuer le mouvement après 100 ms
        self.after(100, self.moveAnt, ant, idImageAnt, targetX, targetY)

            

    # def moveAnt(self, ant, idImageAnt, targetX, targetY):
    #     if ant.x < targetX:
    #         ant.x += 1
    #     elif ant.x > targetX:
    #         ant.x -= 1

    #     if ant.y < targetY:
    #         ant.y += 1
    #     elif ant.y > targetY:
    #         ant.y -= 1


    #     # TODO on recupere l'angle de rotation actuel
    #     # TODO on calcule l'angle de rotation a appliquer
    #     # TODO on applique la rotation

    #     self.canvas.move(idImageAnt, ant.x, ant.y)
    #     self.after(100, self.moveAnt, ant, idImageAnt, targetX, targetY)
            
       
if __name__ == "__main__":
    w = Window()
    w.mainloop()
