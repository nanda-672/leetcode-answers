class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_digit = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]
        }
        result = None
        for num in digits:
            if result is not None:
                added_arr = phone_digit[num]
                old_result = result
                result = []
                for strings in old_result:
                    for char in added_arr:
                        result.append(strings+char)

            else:
                result = phone_digit[num]
            
        return result