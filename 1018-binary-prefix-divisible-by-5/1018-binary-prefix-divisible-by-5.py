class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        # 'current_remainder' will store the remainder of the binary prefix 
        # (up to the current digit) when divided by 5.
        current_remainder = 0
        
        # 'result' will store the boolean answers for each prefix.
        result = []
        
        # Iterate through each digit (0 or 1) in the input array.
        for digit in nums:
            # 1. Update the remainder:
            # To append a new binary digit 'digit', the current prefix value 
            # is shifted left (multiplied by 2) and the new digit is added.
            # We take the modulo 5 at each step to keep the number small.
            current_remainder = (current_remainder * 2 + digit) % 5
            
            # 2. Check for divisibility:
            # A number is divisible by 5 if and only if its remainder is 0.
            result.append(current_remainder == 0)
            
        return result
