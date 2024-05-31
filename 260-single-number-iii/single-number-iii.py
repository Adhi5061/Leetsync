class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all numbers to get the XOR of the two unique numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Step 2: Find a bit that is set (1) in the XOR result
        # This bit is different between the two unique numbers
        set_bit = xor_all & -xor_all  # This isolates the rightmost set bit
        
        # Step 3: Divide numbers into two groups and XOR within each group
        num1, num2 = 0, 0
        for num in nums:
            if num & set_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        # The two unique numbers are num1 and num2
        return [num1, num2]
