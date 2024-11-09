from tabulate import tabulate
from colorama import Fore, Style

class DataDisplay:
    @staticmethod
    def show_table(data):
        table = [[item['id'], item['title']] for item in data]
        print(Fore.GREEN + Style.BRIGHT + "Posts" + Style.RESET_ALL)
        print(tabulate(table, headers=["ID", "Title"], tablefmt="grid"))

    @staticmethod
    def show_users(users):
        table = []
        for user in users:
            table.append([
                user["id"],
                user["name"],
                user["username"],
                user["email"],
                f"{user['address']['street']}, {user['address']['suite']}, {user['address']['city']}, {user['address']['zipcode']}",
                user["phone"],
                user["website"],
                user["company"]["name"]
            ])
        print(Fore.CYAN + Style.BRIGHT + "Users" + Style.RESET_ALL)
        print(tabulate(table, headers=["ID", "Name", "Username", "Email", "Address", "Phone", "Website", "Company"], tablefmt="grid"))

    @staticmethod
    def show_comments(comments):
        table = []
        for comment in comments:
            # Перевірка наявності очікуваних ключів і визначення альтернативного ключа "body"
            comment_text = comment.get('comment') or comment.get('body')
            table.append([
                comment.get('id', 'N/A'), 
                comment.get('postId', 'N/A'), 
                comment.get('userId', 'N/A'), 
                comment_text
            ])
        print(Fore.YELLOW + Style.BRIGHT + "Comments" + Style.RESET_ALL)
        print(tabulate(table, headers=["ID", "Post ID", "User ID", "Comment"], tablefmt="grid"))

