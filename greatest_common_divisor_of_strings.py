import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Проверяем, можно ли найти общий делитель
        if str1 + str2 != str2 + str1:
            return ""
        # Вычисляем НОД длин строк
        g = math.gcd(len(str1), len(str2))
        # Возвращаем префикс str1 длины g
        return str1[:g]

# Примеры для проверки (можно не включать при отправке на LeetCode)
if __name__ == "__main__":
    sol = Solution()
    print(sol.gcdOfStrings("ABCABC", "ABC"))  # "ABC"
    print(sol.gcdOfStrings("ABABAB", "ABAB")) # "AB"
    print(sol.gcdOfStrings("LEET", "CODE"))   # ""
    print(sol.gcdOfStrings("AAAAAB", "AAA"))  # ""
