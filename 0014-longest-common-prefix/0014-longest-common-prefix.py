class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
            
        # Take the first string as a reference point for comparison
        first_str = strs[0]
        
        for i in range(len(first_str)):
            char = first_str[i]
            
            # Compare this character with the character at the same index in all other strings
            for string in strs[1:]:
                # If the current index exceeds the string's length or characters don't match
                if i == len(string) or string[i] != char:
                    return first_str[:i]
                    
        return first_str