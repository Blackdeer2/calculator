import os
import shutil
from BLL.constants import ansi_colors
from Sources.ABC123hash import draw_char_hash
from Sources.ABC123dog import draw_char_dog
from Sources.ABC123asterism import draw_char_asterism

class MyAsciiArtGenerator:
    def __init__(self):
        self.art_text = ""
        #self.font = "standard"
        self.color = "white"
        self.width_factor = 1  
        self.height_factor = 1  
        self.art_symbol = "" 
        self.ascii_text = ""
        self.max_width = 140
        self.max_height = 28
        self.alignment = "center"

    def get_input(self):
        while True:
            text = input("Enter the text you want to convert to ASCII art: ").strip()
            if text:
                self.art_text = text.upper()
                break
            else:
                print("Input cannot be empty. Please try again.") 

    def get_color(self):
        example_colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        print("Available colors: ", ', '.join(example_colors))
        while True:
            color = input("Select a color (or press Enter for 'white'): ").strip()
            if not color:
                self.color = "white"
                break
            elif color in example_colors:
                self.color = color
                break
            else:
                print("Invalid color. Try again.")     

    def get_scaling_factors(self):
        while True:
            try:
                width_factor = input("Enter the width scaling factor (default is 1): ").strip()
                height_factor = input("Enter the height scaling factor (default is 1): ").strip()
                self.width_factor = int(width_factor) if width_factor else 1
                self.height_factor = int(height_factor) if height_factor else 1

                if self.width_factor > 0 and self.height_factor > 0:
                    break
                else:
                    print("Scaling factors must be positive integers. Try again.")
            except ValueError:
                print("Invalid input. Please enter valid integers for scaling factors.")

    def get_symbol(self):
        while True:
            symbol = input("Enter the symbol you want to use in the ASCII art ('@', '#', '*'): ").strip()
            if symbol:
                self.art_symbol = symbol
                break
            else:
                print("Using default symbol '#' for the ASCII art.")
                self.art_symbol = "#"

    def scale_ascii_art(self, ascii_art):
        scaled_lines = []
        for line in ascii_art.splitlines():
            scaled_line = "".join(char * self.width_factor for char in line)
            for _ in range(self.height_factor):
                scaled_lines.append(scaled_line)
        return "\n".join(scaled_lines)
        
    def figlet_format(self, art_text, font):
            result = [""] * 7  

            for letter in art_text:
                if font == "#":
                    letter_art = draw_char_hash(letter)
                elif font == "@":
                    letter_art = draw_char_dog(letter)
                elif font == "*":
                    letter_art = draw_char_asterism(letter)
                else:
                    raise ValueError("Invalid font symbol. Choose '#', '@', or '*'.")
                
                for i in range(7):
                    result[i] += letter_art[i]  

            return "\n".join(result)
            # for line in result:
            #     print(line)
            # print()
    
    # def align_text(self, art, alignment, width):
    #         lines = art.split('\n')
    #         aligned_art = ""
    #         for line in lines:
    #             if alignment == 'center':
    #                 aligned_art += line.center(width) + '\n'
    #             elif alignment == 'left':
    #                 aligned_art += line.ljust(width) + '\n'
    #             elif alignment == 'right':
    #                 aligned_art += line.rjust(width) + '\n'
    #         return aligned_art
    
    def generate_art_symbol(self):
        try:
            ascii_art = self.figlet_format(self.art_text, self.art_symbol)
            scaled_art = self.scale_ascii_art(ascii_art)
            color_code = ansi_colors.ANSI_COLORS.get(self.color, '\033[37m')  
            colored_art = f"{color_code}{scaled_art}\033[0m"
            ascii_art = colored_art.replace("#", self.art_symbol)
            self.ascii_text = ascii_art

            canvas_width, canvas_height = self.get_canvas_size()
            canvas = self.create_canvas(canvas_width, canvas_height)

            art_lines = ascii_art.splitlines()
            for i in range(min(canvas_height, len(art_lines))):
                for j in range(min(canvas_width, len(art_lines[i]))):
                    canvas[i][j] = art_lines[i][j]

            # Виводимо результат
            for line in canvas:
                print(''.join(line))

            return canvas


            # print(ascii_art)
            # return ascii_art
        except Exception as e:
            print(f"Error  generating ASCII art: {e}")
            return None

    # def preview_art(self):
    #     art_preview = self.generate_art()
    #     if art_preview:
    #         print("Preview of your ASCII art:")
    #         print(art_preview)

    def save_to_file(self):
        try:
            folder_to_save = os.path.abspath(os.path.join(os.getcwd(), os.pardir, "calculator", "Sources"))
            os.makedirs(folder_to_save, exist_ok=True) 
            file_name = input("Enter the file name to save the ASCII art (e.g., art): ").strip()
            formatted_file_name = os.path.join(folder_to_save, f"{file_name}.txt")
            ascii_art = self.ascii_text  
            
            with open(formatted_file_name, 'w') as file:
                file.write(ascii_art.replace('\033[0m', ''))  

            print(f"ASCII art saved to {formatted_file_name}.")
        except Exception as e:
            print(f"Error saving ASCII art to file: {e}")

    def align_text(art, alignment='center', width=80):
        lines = art.split('\n')
        aligned_art = ""
        for line in lines:
            if alignment == 'center':
                aligned_art += line.center(width) + '\n'
            elif alignment == 'left':
                aligned_art += line.ljust(width) + '\n'
            elif alignment == 'right':
                aligned_art += line.rjust(width) + '\n'
        return aligned_art
    
    def get_canvas_size(self):
        while True:
            try:
                width = int(input("Enter the width of the canvas (max 140): ").strip())
                height = int(input("Enter the height of the canvas (max 28): ").strip())
                
                if 1 <= width <= 140 and 1 <= height <= 28:
                    return width, height
                else:
                    print("Width must be between 1 and 140, height must be between 1 and 28. Please try again.")
            except ValueError:
                print("Invalid input. Please enter valid integers for width and height.")
    
    def create_canvas(self, width, height):
        return [[' ' for _ in range(width)] for _ in range(height)]
    

    def run(self):
        while True:
            self.get_input()
            self.get_symbol()
            self.get_color()
            self.get_scaling_factors()
            #self.align_text()
            self.generate_art_symbol()

            save_choice = input("Do you want to save the ASCII art to a file? (yes/no): ").strip().lower()
            if save_choice == 'yes':
                self.save_to_file()

            if input('Do you want to create another ASCII art? (yes/no): ').lower() != 'yes':
                print("Thank you for using the ASCII Art Generator!")
                break
