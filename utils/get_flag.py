

def get_flag(country_code):
    # Получаем региональные индикаторы для каждой буквы
    return ''.join(chr(0x1F1E6 + ord(char) - ord('A')) for char in country_code.upper())