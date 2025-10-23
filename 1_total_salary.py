from pathlib import Path

def total_salary(path):
    salaries = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                salaries.append(int(salary))

        total = sum(salaries)
        average = total / len(salaries)

        return total, int(average)

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return 0, 0


file_path = Path('./Temp/text_data.txt')
total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}\nСередня заробітна плата: {average}")
