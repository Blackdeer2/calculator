from constants import global_value
import BLL.functions as functions


class Calculator:
    def __init__(self):
        self.memory_value = global_value.memory_value

    def get_input(self):
        while True:
            try:
                user_input = input('Input first operand (or MR for memory recall): ').upper()
                if user_input == 'MR':
                    first_operand = self.memory_value
                    print(f"Recalled from memory: {first_operand}")
                else:
                    first_operand = float(user_input)

                operator = input("Input operator (+, -, *, /, ^, %, sq): ").strip()
                if not self.validate_operator(operator):
                    print("Invalid operator. Try again.")
                    continue

                while True:
                    user_input = input('Input second operand (or MR for memory recall): ').upper()
                    if user_input == 'MR':
                        second_operand = self.memory_value
                        print(f"Recalled from memory: {second_operand}")
                    else:
                        second_operand = float(user_input)

                    # Якщо обраний оператор - це ділення, перевіряємо, чи другий операнд не дорівнює нулю
                    if operator == '/' and second_operand == 0:
                        print("Error: Division by zero is not allowed. Please enter a non-zero second operand.")
                    else:
                        break  # Вихід з циклу, якщо другий операнд правильний

                return first_operand, second_operand, operator

            except ValueError:
                print("Invalid number format. Try again.")


    def validate_operator(self, operator):
            valid_operators = ['+', '-', '*', '/', '^', '%', 'sq']
            return operator in valid_operators

    def calculate(self, first_operand, second_operand, operator):
        try:
            match operator:
                case '+':
                    result = functions.addition(first_operand, second_operand)
                case '-':
                    result = functions.subtraction(first_operand, second_operand)
                case '/':
                    if second_operand == 0 :
                        raise ZeroDivisionError("Error: Division by zero is not possible.")
                    result = functions.division(first_operand, second_operand)
                case '*':
                    result = functions.multiplication(first_operand, second_operand)
                case '^':
                    result = functions.power(first_operand, second_operand)
                case 'sq':
                    if first_operand < 0:
                            raise ValueError("Error: Negative number under the root.")
                    result = functions.square_root(first_operand, second_operand)
                case '%':
                    result = functions.modulus(first_operand, second_operand)

            functions.log_history(first_operand, operator, second_operand, round(result,global_value.round_number))
            return round(result,global_value.round_number)
        
        except (ZeroDivisionError, ValueError) as e:
            print(e)

    def run(self):


        while True:

            first_operand, second_operand , operator = self.get_input()
            result = self.calculate(first_operand, second_operand, operator)
            if result is not None:
                print(f"Результат: {result}")

            choice_memory = input('Would you like to store result in memory (MS), add to memory (M+), clear memory (MC), or skip? ').upper()
            match choice_memory:
                case 'MS':
                    memory_value = result
                    print(f"Stored {result} in memory.")
                case 'M+':
                    memory_value += result
                    print(f"Added {result} to memory. New memory value: {memory_value}.")
                case 'MC':
                    memory_value = 0
                    print("Memory cleared.")

            if input("Do you want to view history? (yes/no): ").strip().lower() == 'yes':
                print(functions.show_history())
            
            if input('Do you want to make another calculation? (yes/no): ').lower() !='yes':
                break
