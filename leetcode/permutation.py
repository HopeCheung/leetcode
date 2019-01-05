class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0:
            for j in range(i+1, len(nums)): 
                #从后往前， 寻找可替换的最低位
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    #确保替换为的后续位的值最小
                    reg = nums[i+1:]
                    reg.sort()
                    nums[i+1:] = reg
                    return 
            #若当前位不可替换，则自当前位开始排序，以保证下一位可以在不进行完整遍历的前提下找到最小的更大值
            reg = nums[i:]
            reg.sort()
            nums[i:] = reg
            i = i -1

    def Permutation(self,nums):
        def helper(nums, visited)
            if nums in visited:
                return visited
            else:
                visited.append(nums)
                return helper(self.nextPermutation(nums[:]), visited) 
        return helper(nums, [])
    
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def factorial(n):
            if n == 1:
                return 1
            elif n == 0:
                return 0
            else:
                return n * factorial(n-1)
            
        dic = {1:'1', 2:'2',3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'} 
        backup = list(range(1, n+1))
        
        count, curr_num, comparable = 0, [], factorial(n-1)
        while n > 0:
            if k > comparable and comparable != 0:
                k = k - comparable
                count = count + 1
            else:
                curr_num = curr_num + [backup[count]]
                backup.remove(backup[count])
                count = 0
                n = n - 1
                if n == 0:
                    comparable = 0
                else:
                    comparable = comparable // n
        
        result = ''
        for elem in curr_num:
            result = result + dic[elem]
        return result
