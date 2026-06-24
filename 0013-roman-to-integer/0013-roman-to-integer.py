class Solution:
    def romanToInt(self, s: str) -> int:
        # Standard symbol mapping
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            current_val = roman_map[s[i]]
            
            # Check if we are not at the last character and the current value 
            # is less than the next character's value
            if i < n - 1 and current_val < roman_map[s[i + 1]]:
                total -= current_val
            else:
                total += current_val
                
        return total