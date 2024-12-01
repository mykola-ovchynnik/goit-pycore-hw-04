from pathlib import Path
import task_3

FILE_PATH = Path(__file__).resolve().parent

FILE_PATH_SALARY = FILE_PATH / "employees.txt"
FILE_PATH_CATS = FILE_PATH / "cats.txt"


def read_file(path):
    data = []
    try:
        with open(path, "r", encoding="UTF-8") as file:
            data = file.readlines()
    except FileNotFoundError:
        print(f"File {path} not found")
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit()

    return data


def total_salary(path):
    data = read_file(path)

    employees = {}
    for item in data:
        item = item.strip().split(",")
        employees[item[0]] = int(item[1])

    total_salary = sum(employees.values())
    average_salary = total_salary / len(employees)

    return total_salary, average_salary


def get_cats_info(path):
    data = read_file(path)

    result = []
    for line in data:
        id, name, age = line.strip().split(",")
        result.append({"id": id, "name": name, "age": age})

    return result


def main():
    # task 1
    total, average = total_salary(FILE_PATH_SALARY)

    if total is not None and average is not None:
        print(
            f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
        )

    # task 2
    cats_info = get_cats_info(FILE_PATH_CATS)
    print(cats_info)

    # task 3
    task_3.print_directory_structure(FILE_PATH)


if __name__ == "__main__":
    main()
