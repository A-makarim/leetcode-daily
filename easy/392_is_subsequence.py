class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        sub = False
        lastpos = -1
        if s == "":
            return True
        for i in s:
            index = -1

            for  j in t: 
                index = index + 1 
                sub = False # if you dont find it 
                if i == j: 
                    if index > lastpos:
                        lastpos = index
                        sub = True
                        break
            if sub == False:    
                return sub
        return sub
        