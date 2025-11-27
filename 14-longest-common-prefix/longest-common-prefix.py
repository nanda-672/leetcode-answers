class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(len(strs[0])):
            valid = True
            for string in strs:
                if len(prefix) > len(string):
                    valid = False
                else:
                    if prefix != string[:len(prefix)]:
                        valid = False
            if valid:
                return prefix
            else:
                prefix = prefix[:-1]
        return prefix
