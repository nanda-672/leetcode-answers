class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        for char in s:
            if char == " ":
                words.append(word)
                word = ""
            else:
                word += char
        words.append(word)

        words.reverse()
        final_s = ""
        for word in words:
            if word != "":
                final_s += word
                final_s += " "
        return final_s.rstrip()