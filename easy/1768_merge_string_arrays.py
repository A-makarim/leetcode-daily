class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len1 = len(word1)
        len2 = len(word2)
        out = []

        if len1< len2:
            for i in range(len1):
                out.append(word1[i])
                out.append(word2[i]) 
            for j in range(i + 1, len(word2)):
                out.append(word2[j])
        
        else:
            for i in range(len2):
                out.append(word1[i])
                out.append(word2[i])
            for j in range(i + 1, len(word1)):
                out.append(word1[j])
        
        return "".join(out)

        

        
        