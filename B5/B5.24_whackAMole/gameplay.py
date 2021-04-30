import tkinter as tk
import math
import PIL.Image
import PIL.ImageTk


class Game:
    def __init__(self, settings_dict):
        self.data = settings_dict
        self.win = tk.Tk()
        self.win.title("Whack-a-Mole")
        self.win.geometry('512x512')
        self.win.minsize(512, 512)

        x = y = 256
        image0 = PIL.ImageTk.PhotoImage(PIL.Image.open('sprite_0.png'))
        image1 = PIL.ImageTk.PhotoImage(PIL.Image.open('sprite_1.png'))
        image2 = PIL.ImageTk.PhotoImage(PIL.Image.open('sprite_2.png'))
        self.image_list = [image0, image1, image2]

        self.win.mainloop()

    # def nearest_square(self):
    #     value = self.data['num_moles']
    #     i = 2
    #     while i < value:
    #         square = i * i
    #         if square == value:
    #             return square
    #         i += 1
    #         value -= 1
    def layout(self):
        


if __name__ == '__main__':
    settings = {"num_moles": 9,
                "min_under": 1,
                "max_under": 5,
                "min_above": 1,
                "max_above": 3,
                "time": 30}
    game = Game(settings)
    game.layout()
