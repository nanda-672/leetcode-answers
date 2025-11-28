class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ref_word = word
        counter = 0
        while ref_word in sequence:
            counter += 1
            ref_word += word
        return counter
        