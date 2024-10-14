from PIL import Image, ImageTk

class AntDisplay:
    def __init__(self, canvas, ant):
        self.canvas = canvas
        self.ant = ant
        self.images = [
            Image.open("./imgs/ant1.png").resize((50, 50)), 
            Image.open("./imgs/ant2.png").resize((50, 50)),
            Image.open("./imgs/ant3.png").resize((50, 50))
        ]
        self.tk_images = [ImageTk.PhotoImage(img) for img in self.images]
        self.indexCurrentImage = 0
        self.image_id = self.canvas.create_image(ant.x, ant.y, image=self.tk_images[self.indexCurrentImage])

    def nextImage(self):
        self.indexCurrentImage = (self.indexCurrentImage + 1) % len(self.tk_images)

    def getTkImage(self):
        return self.tk_images[self.indexCurrentImage]

    def updatePosition(self):
        self.canvas.coords(self.image_id, self.ant.x, self.ant.y)
        self.canvas.itemconfig(self.image_id, image=self.getTkImage())  
    
    def updateImageAngle(self):
        self.tk_images[self.indexCurrentImage] = ImageTk.PhotoImage(self.images[self.indexCurrentImage].rotate(self.ant.angle))
        self.canvas.itemconfig(self.image_id, image=self.getTkImage())