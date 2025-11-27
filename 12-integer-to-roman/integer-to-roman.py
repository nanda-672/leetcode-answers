class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = {1:"I", 2:"II", 3:"III", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 10:"X", 20:"XX", 30:"XXX", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 100:"C", 200:"CC", 300:"CCC", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 1000:"M", 2000:"MM", 3000: "MMM",4:"IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM"}

        roman_num = ""
        divider = 10
        while num > 0:
            temp = num % divider
            if temp == 0:
                divider *= 10
                pass
            else:
                roman_num = roman_map[temp] + roman_num
                divider *= 10
                num -= temp
        return roman_num
        