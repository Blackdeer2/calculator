from BLL.classes.MyAsciiArtGenerator import MyAsciiArtGenerator
from Sources.ABC123hash import draw_char_hash
from Sources.ABC123dog import draw_char_dog
from Sources.ABC123asterism import draw_char_asterism
# до 13 рядка
# h 28
# w 160
# по центру то побрібно відняти по 10 з двох сторін то w = 140


def main():

    art = MyAsciiArtGenerator()
    art.run()
    # lol = figlet_format("ABC123", "#")

    # print(lol)


main()