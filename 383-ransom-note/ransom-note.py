class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        for char in magazine:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        
        for char in ransomNote:
            if char not in counter:
                return False
            elif counter[char] == 1:
                del counter[char]
            else:
                counter[char] -= 1
        return True
        