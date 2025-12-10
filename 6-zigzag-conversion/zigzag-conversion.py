class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        counter = 0
        direction_down = True
        array = [[] for i in range(numRows)]
        # print(array)
        for char in s:
            array[counter].append(char)

            if counter == numRows-1 and direction_down:
                direction_down = False
                counter -= 1
            
            elif counter == 0 and not direction_down:
                direction_down = True
                counter += 1
            
            elif direction_down:
                counter += 1
            
            elif not direction_down:
                counter -= 1

        ans = ''
        for i in range(numRows):
            ans += ''.join(array[i])

        return ans        