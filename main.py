import functions
import app_settings
from classes.calculator import Calculator

def main():

    calculator = Calculator()
    while True:
        functions.show_menu()
        choice = input('Enter your choice: ').strip()

        match choice:
            case '1':
                calculator.run()
            case '2':
                app_settings.setting()
            case '0':
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")


main()