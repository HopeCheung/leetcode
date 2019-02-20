class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        dic_b, dic_c = {}, {}
        for elem in set(guess):
            dic_c[elem] = min(secret.count(elem), guess.count(elem))

        for i, j in zip(secret, guess):
            if i == j:
                dic_b[i], dic_c[i] = dic_b.get(i, 0) + 1, dic_c[i] - 1
                
        return str(sum(dic_b.values())) + "A" + str(sum(dic_c.values())) + "B"
                
        