


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = [1000,500,100, 50, 10, 5,1]
        symbol = ["M","D","C", "L", "X", "V","I" ]
        num = 0
        last = 0
        for i in s:
            for j in symbol:
                if j == i:
                    arraypos = symbol.index(j)
                    if value[arraypos] > last:
                        num = num - last - last
                        last = value[arraypos]
                        num = num + last
                        break

                    else:
                        last =value[arraypos]
                        num = num + last
                        break
        return num
        
        
        
        print(num)
    

      

        