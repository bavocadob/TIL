class Solution:
    def isPalindrome(self, s: str) -> bool:
        start_idx = 0
        end_idx = len(s) - 1
        while start_idx <= end_idx:
            if not s[start_idx].isalnum():
                start_idx += 1
                continue

            if not s[end_idx].isalnum():
                end_idx -= 1
                continue

            if s[start_idx].isalpha() and s[end_idx].isalpha():
                if s[start_idx].lower() != s[end_idx].lower():
                    return False
            elif s[start_idx].isdigit() and s[end_idx].isdigit():
                if s[start_idx] != s[end_idx]:
                    return False
            else:
                return False

            start_idx += 1
            end_idx -= 1
        return True
