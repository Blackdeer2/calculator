from BLL.classes.MyAsciiArtGenerator import MyAsciiArtGenerator
from Sources.ABC123hash import draw_char_hash
from Sources.ABC123dog import draw_char_dog
from Sources.ABC123asterism import draw_char_asterism
# до 13 рядка
# h 28
# w 160
# по центру то побрібно відняти по 10 з двох сторін то w = 140
def figlet_format(art_text, font):
            result = [""] * 7  

            for letter in art_text:
                if font == "#":
                    letter_art = draw_char_hash(letter)
                elif font == "@":
                    letter_art = draw_char_dog(letter)
                elif font == "*":
                    letter_art = draw_char_asterism(letter)
                
                for i in range(7):
                    result[i] += letter_art[i]  

            return "\n".join(result)
            # for line in result:
            #     print(line)
            # print()




def main():

    art = MyAsciiArtGenerator()
    art.run()
    # lol = figlet_format("ABC123", "#")

    # print(lol)


main()