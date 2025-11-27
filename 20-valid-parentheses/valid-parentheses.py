class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_open_map = {"(":")", "[":"]", "{":"}"}
        parentheses_open = ["(","[","{"]
        parentheses_close_map = {")":"(", "]":"[", "}":"{"}
        parentheses_close = [")", "]", "}"]

        lookup_stack = []

        if len(s)%2 != 0:
            return False

        for parentheses in s:
            if parentheses in parentheses_open:
                lookup_stack.append(parentheses_open_map[parentheses])
            if parentheses in parentheses_close:
                if len(lookup_stack) != 0:
                    if lookup_stack.pop() != parentheses:
                        return False
                else:
                    return False
                    
        if len(lookup_stack) != 0:
            return False
        return True