from tabulate import tabulate
from BLL.ErrorHandler import ErrorHandler
from APIClient import APIClient
from BLL.classes.DataDisplay import DataDisplay
from DAL.DataSaver import DataSaver
from DAL.HistoryLogger import HistoryLogger
from UI.UserInterface import UserInterface


def main():
    client = APIClient()
    ui = UserInterface()
    display = DataDisplay()
    saver = DataSaver()
    logger = HistoryLogger()

    while True:
        ui.display_menu()
        choice = ui.get_user_input()

        if choice == '1':  # Показати всі пости
            try:
                posts = client.get_data("posts")
                display.show_table(posts)
                logger.log("показати всі пости", posts)
            except Exception as e:
                ErrorHandler.handle_error(e)

        elif choice == '2':  # Показати пост за ID
            try:
                post_id = input("Введіть ID поста: ")
                post = client.get_data_by_id("posts", post_id)
                display.show_table([post])  # Вивести один запис як таблицю
                logger.log(f"показати пост з ID {post_id}", post)
            except Exception as e:
                ErrorHandler.handle_error(e)

        elif choice == '3':  # Зберегти дані
            format_choice = input("Введіть формат збереження (json/csv/txt): ").strip().lower()
            filename = input("Введіть ім'я файлу: ").strip()
            if format_choice == 'json':
                saver.save_as_json(posts, filename)
            elif format_choice == 'csv':
                saver.save_as_csv(posts, filename)
            elif format_choice == 'txt':
                saver.save_as_txt(posts, filename)
            else:
                print("Невідомий формат.")
            print(f"Дані збережено у {filename}.{format_choice}")

        elif choice == '4':  # Показати всіх користувачів
            try:
                users = client.get_all_users()
                display.show_users(users)
                logger.log("показати всіх користувачів", users)
            except Exception as e:
                ErrorHandler.handle_error(e)

        elif choice == '5':  # Показати користувача за ID
            try:
                user_id = input("Введіть ID користувача: ")
                user = client.get_user_by_id(user_id)
                display.show_users([user])
                logger.log(f"показати користувача з ID {user_id}", user)
            except Exception as e:
                ErrorHandler.handle_error(e)

        elif choice == '6':  # Показати всі коментарі
            try:
                comments = client.get_all_comments()
                display.show_comments(comments)
                logger.log("показати всі коментарі", comments)
            except Exception as e:
                ErrorHandler.handle_error(e)

        elif choice == '7':  # Показати коментар за ID
            try:
                comment_id = input("Введіть ID коментаря: ")
                comment = client.get_comment_by_id(comment_id)
                display.show_comments([comment])
                logger.log(f"показати коментар з ID {comment_id}", comment)
            except Exception as e:
                ErrorHandler.handle_error(e)

        elif choice == '8':  # Показати історію
            logger.show_history()

        elif choice == '0':  # Вийти
            print("Вихід...")
            break

        else:
            print("Невідома команда, спробуйте ще раз.")

if __name__ == "__main__":
    main()