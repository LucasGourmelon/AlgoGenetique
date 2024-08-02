import tkinter as tk
from itertools import cycle

class Ant:
    def __init__(self, canvas, x, y, images):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.images = cycle(images)  # Cycle through the images
        self.current_image = next(self.images)
        self.image_id = self.canvas.create_image(x, y, image=self.current_image)
        self.state = 'Stop'  # Initial state

    def update_image(self):
        if self.state == 'Walk':
            # Change to the next image in the cycle
            self.current_image = next(self.images)
            self.canvas.itemconfig(self.image_id, image=self.current_image)

    def set_state(self, new_state):
        """Set the state to either 'Walk' or 'Stop'."""
        if new_state in ['Walk', 'Stop']:
            self.state = new_state

class Window:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()

        # Load images
        self.ant_images = [
            tk.PhotoImage(file='./imgs/ant1.png'),
            tk.PhotoImage(file='./imgs/ant2.png'),
            tk.PhotoImage(file='./imgs/ant3.png')
        ]

        self.ant = Ant(self.canvas, 400, 300, self.ant_images)

        # Buttons to change ant's state
        self.start_button = tk.Button(root, text="Start Walking", command=lambda: self.ant.set_state('Walk'))
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop Walking", command=lambda: self.ant.set_state('Stop'))
        self.stop_button.pack()

        self.animate()

    def animate(self):
        self.ant.update_image()
        self.root.after(1000, self.animate)  # Call this method every 1000 ms (1 second)

if __name__ == "__main__":
    root = tk.Tk()
    window = Window(root)
    root.mainloop()
