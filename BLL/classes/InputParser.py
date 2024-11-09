import re

class InputParser:
    @staticmethod
    def parse_date(input_str):
        if re.match(r'^\d{4}-\d{2}-\d{2}$', input_str):
            return "Дата розпізнана!"
        return "Невірний формат дати"
    
    @staticmethod
    def parse_phone(input_str):
        if re.match(r'^\+?\d[\d -]{7,12}\d$', input_str):
            return "Телефонний номер розпізнано!"
        return "Невірний формат телефону"
