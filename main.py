from BLL.classes.threeD_art_generato import ThreeDArtService
import sys

# gen = ThreeDArtService()

# white = MenuItem("1", "White.", gen.change_color, [0])
# red = MenuItem("2", "Red.", gen.change_color, [91])
# blue = MenuItem("3", "Blue.", gen.change_color, [94])

# change_color_menu = MenuBuilder([white, red, blue])

# create_item = MenuItem("1", "Create a cube.", gen.print_art)
# change_color = MenuItem("2", "Change art color.", change_color_menu.initialize)
# change_size = MenuItem("3", "Change art size.", gen.change_size)
# change_direction = MenuItem("4", "Change art direction.", gen.change_direction)
# save_art = MenuItem("5", "Save art.", gen.save_art_into_file, ["./Data/art.txt"])
# see_art = MenuItem("6", "See previous arts.", gen.get_art_archive, ["./Data/art.txt"])
# exit_menu = MenuItem("9", "Exit.", sys.exit)

# main_menu = MenuBuilder([create_item, change_color, change_size, change_direction, save_art, see_art, exit_menu])

def menu():
    art_service = ThreeDArtService(3, 0, False)

    while True:
        print("\n--- 3D Art Menu ---")
        print("1. Change Cube Size")
        print("2. Change Color")
        print("3. Toggle Art Direction")
        print("4. Display Art")
        print("5. Display 2D Art")
        print("6. Save Art to File")
        print("7. Load and Display Art from File")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            art_service.change_size()
        elif choice == "2":
            new_color = int(input("Enter color code (e.g., 31 for red, 32 for green, 34 for blue): "))
            art_service.change_color(new_color)
        elif choice == "3":
            art_service.change_direction()
        elif choice == "4":
            art_service.print_art()
        elif choice == "5":
            art_service.print_2d_art()
        elif choice == "6":
            file_name = input("Enter file name to save: ")
            art_service.save_art_into_file(file_name)
            print(f"Art saved to {file_name}")
        elif choice == "7":
            file_name = input("Enter file name to load: ")
            try:
                ThreeDArtService.get_art_archive(file_name)
            except FileNotFoundError:
                print("File not found. Please check the file name.")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    menu()



if __name__ == "__main__":
    main()
