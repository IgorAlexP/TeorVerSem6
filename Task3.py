"""Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175
Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей."""


import math

# Рост дочерей и матерей
height_children = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]
height_mothers = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]

# Вычисляем средние значения
mean_children = sum(height_children) / len(height_children)
mean_mothers = sum(height_mothers) / len(height_mothers)

# Вычисляем стандартные отклонения
std_children = math.sqrt(sum((x - mean_children) ** 2 for x in height_children) / (len(height_children) - 1))
std_mothers = math.sqrt(sum((x - mean_mothers) ** 2 for x in height_mothers) / (len(height_mothers) - 1))

# Рассчитываем стандартную ошибку разности средних
standard_error = math.sqrt((std_children ** 2 / len(height_children)) + (std_mothers ** 2 / len(height_mothers)))

# Рассчитываем значение t-статистики для заданного уровня доверия и степеней свободы
t_value = 2.262  # для уровня доверия 0.95 и 18 степеней свободы (10 дочерей + 10 матерей - 2)

# Рассчитываем доверительный интервал для разности средних
lower_bound = (mean_children - mean_mothers) - t_value * standard_error
upper_bound = (mean_children - mean_mothers) + t_value * standard_error

# Выводим результаты
print("Доверительный интервал для разности среднего роста:", (lower_bound, upper_bound))

"""neDrive/Рабочий стол/Stud/TeorVer/Sem6DZ/Task3.py"
Доверительный интервал для разности среднего роста: (-10.694691683055188, 6.894691683055177)"""
