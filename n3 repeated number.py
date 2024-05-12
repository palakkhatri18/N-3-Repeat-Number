class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        
        # Finding candidates for the majority elements
        for num in A:
            if count1 == 0 and num != candidate2:
                candidate1 = num
            elif count2 == 0 and num != candidate1:
                candidate2 = num
                
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Reset counts for accurate counting
        count1, count2 = 0, 0
        
        # Counting occurrences of candidates
        for num in A:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        n = len(A)
        if count1 > n // 3:
            return candidate1
        elif count2 > n // 3:
            return candidate2
        else:
            return -1