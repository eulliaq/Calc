import sys


def calculate(num1: float, num2: float, operation: str):
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*" | "×":
            return num1 * num2
        case "/" | "÷":
            if num2 == 0:
                return "Ошибка: деление на ноль невозможно."
            return num1 / num2
        case "^" | "**":
            try:
                return num1**num2
            except OverflowError:
                return "Ошибка: результат возведения в степень слишком велик."
        case "%":
            if num2 == 0:
                return "Ошибка: нахождение остатка от деления на ноль невозможно."
            return num1 % num2
        case _:
            return "Ошибка: неизвестная операция."


def get_float_input(prompt: str):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ("exit", "q"):
            return "exit"
        try:
            return float(user_input)
        except ValueError:
            print(
                "Ошибка ввода! Пожалуйста, введите корректное число или 'q' для выхода."
            )


def get_operation_input(prompt: str):
    valid_operations = {"+", "-", "*", "×", "/", "÷", "^", "**", "%"}
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() in ("exit", "q"):
            return "exit"
        if user_input in valid_operations:
            return user_input
        print(
            f"Ошибка! Недопустимая операция. Доступные варианты: {', '.join(sorted(valid_operations))}"
        )


def main():
    print("\nКОНСОЛЬНЫЙ КАЛЬКУЛЯТОР")
    print("Инструкция:", "\n1. Вводите данные пошагово (число, операция, число).", "\n2. Поддерживаемые операции: +, -, *, ×, /, ÷, ^, **, %", "\n3. Для выхода из программы введите 'exit' или 'q' на любом шаге.")
    print("-" * 50)

    while True:
        print("\n--- Новое вычисление ---")

        num1 = get_float_input("Введите первое число: ")
        if num1 == "exit":
            break

        operation = get_operation_input("Введите операцию (+, -, *, /, ^, %): ")
        if operation == "exit":
            break

        num2 = get_float_input("Введите второе число: ")
        if num2 == "exit":
            break

        result = calculate(num1, num2, operation)

        if isinstance(result, str):
            print(result)
        else:
            if result.is_integer():
                print(f"Результат: {int(result)}")
            else:
                print(f"Результат: {result}")

    print("\nПрограмма завершена.")


if __name__ == "__main__":
    main()
