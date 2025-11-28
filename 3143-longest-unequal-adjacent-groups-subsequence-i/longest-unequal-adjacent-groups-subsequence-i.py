class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        subsequence = []
        memo = -1
        for i in range(len(words)):
            if groups[i] != memo:
                memo = groups[i]
                subsequence.append(words[i])
        return subsequence            