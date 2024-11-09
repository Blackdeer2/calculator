class UserInterface:
    def display_menu(self):
        print("1. Показати всі пости")
        print("2. Показати пост за ID")
        print("3. Зберегти дані")
        print("4. Показати всіх користувачів")  
        print("5. Показати користувача за ID")  
        print("6. Показати всі коментарі")  
        print("7. Показати коментар за ID")  
        print("8. Показати історію запитів")
        print("0. Вийти")
    
    def get_user_input(self):
        choice = input("Введіть номер команди: ")
        return choice