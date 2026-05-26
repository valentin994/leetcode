class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        roman_sum = 0
        prev = 0
        for el in reversed(s):
            curr_value = roman_values[el]
            if curr_value < prev:
                roman_sum -= curr_value
            else:
                roman_sum += curr_value
            prev = curr_value
        return roman_sum


s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))
