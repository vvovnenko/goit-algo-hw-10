import random
import scipy.integrate as spi


# Визначення функції та межі інтегрування
def f(x):
    return x ** 2


# Перевіряє, чи знаходиться точка (x, y) під кривою.
def is_inside(x, y):
    return f(x) >= y


def monte_carlo_simulation(x1, x2, y1, y2, num_experiments):
    average_area = 0

    for _ in range(num_experiments):
        # Генерація випадкових точок
        points = [(random.uniform(x1, x2), random.uniform(y1, y2)) for _ in range(15000)]
        # Відбір точок, що знаходяться всередині трикутника
        inside_points = [point for point in points if is_inside(point[0], point[1])]

        # Розрахунок площі за методом Монте-Карло
        M = len(inside_points)
        N = len(points)
        area = (M / N) * ((x2 - x1) * (y2 - y1))

        # Додавання до середньої площі
        average_area += area

    # Обчислення середньої площі
    average_area /= num_experiments
    return average_area


x1 = 0  # Нижня межа по осі x
x2 = 2  # Верхня межа по осі x

y1 = 0  # Нижня межа по осі y
y2 = 4  # Верхня межа по осі y

# Кількість експериментів
num_experiments = 100

# Обчислення інтеграла
result = spi.quad(f, x1, x2)[0]

# Виконання симуляції
average_area = monte_carlo_simulation(x1, x2, y1, y2, num_experiments)
print(f"Обраховане значення інтегралу за допомогою quad: {result}")
print(f"Обраховане значення інтегралу за {num_experiments} експериментів методом Монте-Карло: {average_area}")
