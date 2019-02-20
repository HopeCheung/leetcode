class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if len(input) == 0:
            return []
        if input.isdigit():
            return [int(input)]
        
        def helper(num1, num2, op):
            if op == "+":
                return num1 + num2
            elif op == "-":
                return num1 - num2
            elif op == "*":
                return num1 * num2
        
        res = []
        for i in range(len(input)):
            if input[i] in "*-+":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                
                for j in res1:
                    for k in res2:
                        res.append(helper(j, k, input[i]))
        return res
        
        