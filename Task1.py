""" Известно, что генеральная совокупность распределена нормально со средним квадратическим отклонением, равным 16.
Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95, если выборочная средняя M = 80, 
а объем выборки n = 256."""

import math

# Заданные значения
M = 80  # выборочная средняя
n = 256  # объем выборки
sigma = 16  # стандартное отклонение генеральной совокупности
confidence = 0.95  # уровень доверия

# Рассчитываем стандартную ошибку среднего
standard_error = sigma / math.sqrt(n)

# Находим значение Z-статистики для заданного уровня доверия
z_value = 1.96  # для уровня доверия 0.95

# Рассчитываем доверительный интервал
lower_bound = M - z_value * standard_error
upper_bound = M + z_value * standard_error

# Выводим результаты
print("Доверительный интервал:", (lower_bound, upper_bound))


"""c:/Users/clic/OneDrive/Рабочий стол/Stud/TeorVer/Sem6DZ/Task3.py
Доверительный интервал: (78.04, 81.96)"""