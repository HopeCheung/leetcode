class Solution:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def one_max(nums, t):
            stack, i = [], 0
            while i < len(nums):
                while stack and len(stack) + len(nums[i:]) > t and stack[-1] < nums[i]:
                    stack.pop()
                if len(stack) < t:
                    stack.append(nums[i])
                i = i + 1
            return stack
        
        def combine(nums1, nums2):
            if len(nums1) == 0:
                return nums2
            elif len(nums2) == 0:
                return nums1
            else:
                if nums1[0] > nums2[0]:
                    return [nums1[0]] + combine(nums1[1:], nums2)
                elif nums1[0] < nums2[0]:
                    return [nums2[0]] + combine(nums1, nums2[1:])
                else:
                    i = 0
                    while i < len(nums1) and i < len(nums2) and nums1[i] == nums2[i]:
                        i = i + 1
                        
                    if i == len(nums1):
                        return [nums2[0]] + combine(nums1, nums2[1:])
                    elif i == len(nums2):
                        return [nums1[0]] + combine(nums1[1:], nums2)
                    else:
                         if nums1[i] > nums2[i]:
                            return [nums1[0]] + combine(nums1[1:], nums2)
                         elif nums1[i] < nums2[i]:
                            return [nums2[0]] + combine(nums1, nums2[1:])
                
        if nums1 == []:
            return nums2
        if nums2 == []:
            return nums1
        
        rst = []
        for t in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            if t > len(nums1) or k-t > len(nums2):
                continue
            else:
                print(t, one_max(nums1, t), k-t, one_max(nums2, k-t))
                rst.append(combine(one_max(nums1, t), one_max(nums2, k-t)))
        
        return max(rst)
        
                
class Solution:
    def maxNumber(self, nums1, nums2, k):
        def merge(arr1, arr2):
            res, i, j = [], 0, 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i:] >= arr2[j:]:
                    res.append(arr1[i])
                    i += 1
                else: 
                    res.append(arr2[j])
                    j += 1
            if i < len(arr1): res += arr1[i:]
            elif j < len(arr2): res += arr2[j:]
            return res     
        
        def makeArr(arr, l):
            i, res = 0, []
            for r in range(l - 1, -1, -1):
                num, i = max(arr[i:-r] or arr[i:])
                i = -i + 1
                res.append(num)
            return res
        
        nums1, nums2, choices = [(num, -i) for i, num in enumerate(nums1)], [(num, -i) for i, num in enumerate(nums2)], []
        for m in range(k + 1):
            if m > len(nums1) or k - m > len(nums2): continue
            arr1, arr2 = makeArr(nums1, m), makeArr(nums2, k - m)  
            choices.append(merge(arr1, arr2))
        return max(choices)

class Solution:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def one_max(nums, t):
            stack, i = [], 0
            while i < len(nums):
                while stack and len(stack) + len(nums[i:]) > t and stack[-1] < nums[i]:
                    stack.pop()
                if len(stack) < t:
                    stack.append(nums[i])
                i = i + 1
            return stack
        
        def combine(arr1, arr2):
            res, i, j = [], 0, 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i:] >= arr2[j:]:
                    res.append(arr1[i])
                    i += 1
                else: 
                    res.append(arr2[j])
                    j += 1
            if i < len(arr1): res += arr1[i:]
            elif j < len(arr2): res += arr2[j:]
            return res 
                
        if nums1 == []:
            return nums2
        if nums2 == []:
            return nums1
        
        rst = []
        for t in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            if t > len(nums1) or k-t > len(nums2):
                continue
            else:
                #print(t, one_max(nums1, t), k-t, one_max(nums2, k-t))
                rst.append(combine(one_max(nums1, t), one_max(nums2, k-t)))
        
        return max(rst)
    
        
        
        
                
        
