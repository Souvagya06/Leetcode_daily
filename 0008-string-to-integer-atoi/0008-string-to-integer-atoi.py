class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        result = 0
        
        # Define 32-bit signed integer boundaries
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # Step 1: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
            
        # Step 2: Check for sign
        if i < n:
            if s[i] == '-':
                sign = -1
                i += 1
            elif s[i] == '+':
                i += 1
                
        # Step 3: Convert digits and handle Step 4 (Rounding/Overflow)
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Check for 32-bit integer overflow before multiplying
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
            
        return sign * result