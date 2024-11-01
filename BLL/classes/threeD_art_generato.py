import os
from BLL.classes.figures.Cube import Cube
import BLL.classes.FileService as FileService

class ThreeDArtService:
    def __init__(self, height: int, color: int, direction: bool):
        self.art = Cube(height)
        self.color = color
        self.direction = direction

    def change_size(self):
        try:
            size = int(input("Enter new size (no less than 3): "))
            self.art.side_a = size
        except ValueError:
            print("Wrong choice, try again")
            self.change_size()

    def change_color(self, color: int):
        self.color = color

    def change_direction(self):
        self.direction = not self.direction
        print("Direction was successfully changed")

    def get_art(self) -> str:
        color_text = '\033[%dm%s\033[0m'

        art = ""
        if self.direction:
            art = self.art.get_three_d_art()
        else:
            art = self.art.get_three_d_inverted_art()

        return color_text % (self.color, art)
    
    def get_2d_art(self) -> str:
        color_text = '\033[%dm%s\033[0m'
        art = self.art.get_two_d_art()
        return color_text % (self.color, art)

    def print_art(self):
        print(self.get_art())

    def print_2d_art(self):
        print(self.get_2d_art())

    def save_art_into_file(self, file_name: str):
        try:
            FileService.write_into_file(file_name, self.get_art())
        except FileExistsError:
            raise FileExistsError

    @staticmethod
    def get_art_archive(file_name: str):
        try:
            print(FileService.read_from_file(file_name))
        except FileNotFoundError:
            raise FileNotFoundError
    