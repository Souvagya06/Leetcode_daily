from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # Validate palindrome possibility
        odd_chars = [char for char, count in counts.items() if count % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        
        # Build character pool for the first half
        half_counts = {char: count // 2 for char, count in counts.items()}
        half_len = n // 2

        def construct_palindrome(first_half: str) -> str:
            second_half = first_half[::-1]
            return first_half + mid_char + second_half

        # Try matching prefix of length `i` with target, then taking a strictly larger character at `i`
        for i in range(half_len, -1, -1):
            # Check if current prefix target[:i] can be formed by available counts
            prefix = target[:i]
            prefix_counts = Counter(prefix)
            
            # Ensure prefix is valid with available half counts
            if any(prefix_counts[char] > half_counts.get(char, 0) for char in prefix_counts):
                continue
            
            # Remaining character pool for positions >= i
            rem_counts = {char: half_counts[char] - prefix_counts.get(char, 0) for char in half_counts}
            
            # Case 1: Exact prefix match up to half_len
            if i == half_len:
                pal = construct_palindrome(prefix)
                if pal > target:
                    return pal
                continue
            
            # Case 2: At index i, pick a character > target[i]
            target_char = target[i]
            for c in sorted(rem_counts.keys()):
                if c > target_char and rem_counts[c] > 0:
                    # Place character `c` at position i
                    rem_counts[c] -= 1
                    
                    # Fill the rest with the smallest available characters
                    suffix = "".join(sorted([char * count for char, count in rem_counts.items()]))
                    candidate_half = prefix + c + suffix
                    
                    pal = construct_palindrome(candidate_half)
                    if pal > target:
                        return pal
                    
                    rem_counts[c] += 1  # backtrack

        return ""