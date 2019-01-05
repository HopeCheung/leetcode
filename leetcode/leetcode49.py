class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def one_group(str1, str2):
            if str1 == str2:
                return True
            elif set(str1) == set(str2):
                if len(str1) == str1:
                    return True
                else:
                    dic1, dic2 = {}, {}
                    for i in str1:
                        if i in dic1:
                            dic1[i] = dic1[i] + 1
                        else:
                            dic1[i] = 1
                    for j in str2:
                        if j in dic2:
                            dic2[j] = dic2[j] + 1
                        else:
                            dic2[j] = 1
                    return dic1 == dic2
            return False
        
        if len(strs) == 0:
            return
        
        result = []
        while len(strs) > 0:
            one_result = [strs[0]]
            j = 1
            while len(strs) > 0 and j < len(strs):
                if one_group(strs[0], strs[j]):
                    one_result.append(strs[j])
                    if j + 1 < len(strs):
                        strs = strs[0:j] + strs[j+1:]
                    else:
                        strs = strs[0:j]
                else:
                    j = j + 1
            strs = strs[1:]
            result.append(one_result)
            one_result = []
        return result
        
###############------------time limit
class Solution2:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """ 
        def convert(symbol):
            return str(sorted(list(symbol)))
        
        if len(strs) == 0:
            return
        
        dic = {}
        for elem in strs:
            if convert(elem) not in dic:
                dic[convert(elem)] = [elem]
            else:
                dic[convert(elem)].append(elem)
        return [dic[elem] for elem in dic]
            
