
# Class to convert an integer to a roman numeral

class Solution:

    def intToRoman(self, number):
    
        int_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        roman_values = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"] 

        roman_num = ""

        i = 0

        while number > 0:
            for n in range(number//int_values[i]):
                roman_num += roman_values[i]
                number -= int_values[i]
            i += 1
        
        return roman_num

print(Solution().intToRoman(43))









