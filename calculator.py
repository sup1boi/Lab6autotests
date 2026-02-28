import math


class CalculatorError(Exception):
    """Базовое исключение калькулятора."""
    pass


class DivisionByZeroError(CalculatorError):
    """Исключение при делении на ноль."""
    pass


class InvalidInputError(CalculatorError):
    """Исключение при некорректном входном значении."""
    pass


class Calculator:

    @staticmethod
    def _validate_number(value):
        if not isinstance(value, (int, float)):
            raise InvalidInputError(f"Некорректный тип данных: {type(value)}")

    @classmethod
    def add(cls, a, b):
        cls._validate_number(a)
        cls._validate_number(b)
        return a + b

    @classmethod
    def subtract(cls, a, b):
        cls._validate_number(a)
        cls._validate_number(b)
        return a - b

    @classmethod
    def multiply(cls, a, b):
        cls._validate_number(a)
        cls._validate_number(b)
        return a * b

    @classmethod
    def divide(cls, a, b):
        cls._validate_number(a)
        cls._validate_number(b)

        if b == 0:
            raise DivisionByZeroError("Деление на ноль запрещено.")

        return a / b

    @classmethod
    def power(cls, base, exponent):
        cls._validate_number(base)
        cls._validate_number(exponent)
        return base ** exponent

    @classmethod
    def sqrt(cls, value):
        cls._validate_number(value)

        if value < 0:
            raise InvalidInputError("Нельзя извлекать квадратный корень из отрицательного числа.")

        return math.sqrt(value)

    @classmethod
    def factorial(cls, n):
        if not isinstance(n, int):
            raise InvalidInputError("Факториал определён только для целых чисел.")

        if n < 0:
            raise InvalidInputError("Факториал отрицательного числа не определён.")

        return math.factorial(n)

    @classmethod
    def is_prime_number(cls, n):
        if not isinstance(n, int):
            raise InvalidInputError("Проверка простоты возможна только для целых чисел.")

        if n <= 1:
            return False

        if n == 2:
            return True

        if n % 2 == 0:
            return False

        limit = int(math.sqrt(n)) + 1
        for i in range(3, limit, 2):
            if n % i == 0:
                return False

        return True