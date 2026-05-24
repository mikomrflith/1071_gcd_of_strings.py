 LeetCode 75 — Решения задач

Репозиторий содержит решения задач из учебного плана LeetCode 75, выполненные в рамках отчёта по дисциплине «Практикум по программированию».

  Содержание

- [Задача 1071. Greatest Common Divisor of Strings](1071-greatest-common-divisor-of-strings)

---

 1071. Greatest Common Divisor of Strings

Уровень: Easy  
Тема: Строки, Математика (НОД)

 Условие

Для двух строк `str1` и `str2` найдите наибольшую общую строку-делитель `x`, такую что повторением `x` можно получить и `str1`, и `str2`.

 Примеры

| str1       | str2  | Результат |
|------------|-------|-----------|
| `"ABCABC"` | `"ABC"` | `"ABC"`   |
| `"ABABAB"` | `"ABAB"`| `"AB"`    |
| `"LEET"`   | `"CODE"`| `""`      |

 Подход

1. Проверяем, что строки «коммутируют»: `str1 + str2 == str2 + str1`. Если это не так — общего делителя не существует, возвращаем `""`.
2. Находим НОД длин строк: `g = gcd(len(str1), len(str2))`.
3. Возвращаем первые `g` символов строки `str1`.

Сложность: `O(n + m)` по времени и памяти (из-за операций конкатенации), где `n` и `m` — длины строк.

 Реализация (Python)

```python
import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        g = math.gcd(len(str1), len(str2))
        return str1[:g]
