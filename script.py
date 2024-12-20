import re

def replace_symbols_in_file(file_path):
    # Открываем файл для чтения
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Заменяем \[ и \] на $$
    text = re.sub(r'\\\[', '$$', text)
    text = re.sub(r'\\\]', '$$', text)
    
    # Заменяем \( и \) на $
    text = re.sub(r'\\\(', '$', text)
    text = re.sub(r'\\\)', '$', text)
    
    # Открываем файл для записи измененного текста
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

# Путь к вашему файлу
file_path = 't.txt'
replace_symbols_in_file(file_path)

print(f"Изменения успешно внесены в файл {file_path}.")
