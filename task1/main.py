import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Визначення змінних
L = pulp.LpVariable('L', lowBound=0, cat='Integer')  # Кількість Лимонаду
F = pulp.LpVariable('F', lowBound=0, cat='Integer')  # Кількість Фруктового соку

# Функція цілі (Максимізація прибутку)
model += L + F, "Profit"

# Додавання обмежень
model += 2 * L + 1 * F <= 100  # Обмеження для Води
model += 1 * L <= 50  # Обмеження для Цукру
model += 1 * L <= 30  # Обмеження для Лимонного соку
model += 2 * F <= 40  # Обмеження для Фруктового пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти Лимонаду:", L.varValue)
print("Виробляти Фруктового соку:", F.varValue)
