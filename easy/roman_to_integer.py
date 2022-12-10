#https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary that maps Roman numerals to their integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Initialize a result variable to keep track of the integer value
        result = 0

        # Iterate over the characters in the input string
        for i in range(len(s)):
            # Find the integer value of the current character
            current_numeral = roman_to_int[s[i]]

            # If the current character is not the last character in the string
            if i < len(s) - 1:
                # Find the integer value of the next character
                next_numeral = roman_to_int[s[i + 1]]

                # If the next character has a higher value, subtract the current character's value from the result
                # because this indicates that the current character is a "subtractive" numeral (e.g. "IV" = 4)
                if next_numeral > current_numeral:
                    result -= current_numeral

                # Otherwise, add the current character's value to the result because this indicates that the
                # current character is a "regular" numeral (e.g. "VI" = 6)
                else:
                    result += current_numeral
            # If the current character is the last character in the string, add its value to the result because
            # it cannot be a "subtractive" numeral
            else:
                result += current_numeral

        # Return the result as the integer value of the input Roman numeral
        return result

# Test the romanToInt() function

sol = Solution()

# Test 1: "III" => 3
s = "III"
print(sol.romanToInt(s))

# Test 2: "LVIII" => 58
s = "LVIII"
print(sol.romanToInt(s))

# Test 3: "MCMXCIV" => 1994
s = "MCMXCIV"
print(sol.romanToInt(s))
