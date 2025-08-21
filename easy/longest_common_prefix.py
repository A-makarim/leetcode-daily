class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # if any strs is empty, return ""
        # if strs is null, retun ""

        # otherwise, 

        # iterate thru every word. 
        # iterate thru every letter
        # keep the existing letters in buffer till they match new prefixes
        # start with full first word in buffer
        # move onto second, compare buffer until same, initialize buffer. 
        # repeat

        if strs is None:
            return ""

        if len(strs) == 1:
            return strs[0]

        buffer = ""

        for i in range(len(strs)-1): # give me that number of iterations    len 2, 0 , 1
            if i == 0:  
                buffer = strs[i] 
            elif buffer == "":  
                return "" # no need for further
            nextword = strs[i+1]   #moves on 1  #a                    a 
            j = 0
            while j < min(len(buffer), len(nextword)) and buffer[j] == nextword[j]:
                j += 1
            buffer = buffer[0:j] #not same? note j, and break out of loop
        return buffer
