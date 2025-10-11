from pathlib import Path

def get_cats_info(path):
    try:
        with open(path, encoding='utf-8') as f:
            return [
                dict(zip(['id', 'name', 'age'], line.strip().split(',')))
                for line in f
            ]
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []

file_path = Path('./Temp/cats.txt')
cats_info = get_cats_info(file_path)
print(cats_info)
