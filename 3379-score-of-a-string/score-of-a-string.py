class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        char_seen = {}
        for i in range(len(s)-1):
            if s[i] not in char_seen:
                char_seen[s[i]] = ord(s[i])
            if s[i+1] not in char_seen:
                char_seen[s[i+1]] = ord(s[i+1])
            score += abs(char_seen[s[i]] - char_seen[s[i+1]])
        return score
        