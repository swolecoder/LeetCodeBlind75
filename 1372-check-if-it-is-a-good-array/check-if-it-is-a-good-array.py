class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:

# To provide a clearer understanding without using built-in functions, let's dive into a more detailed explanation and manually implement the logic needed to solve the problem. The core concept revolves around the Greatest Common Divisor (GCD), which is the largest number that divides two numbers without leaving a remainder. For an array to be "good," we need to find if there's a set of numbers in it whose GCD is 1. This is because any set of numbers that can have their GCD reduced to 1 can linearly combine (using some multiplication and addition) to form any integer, including 1.

# ### Understanding GCD and Bezout's Identity

# A key mathematical principle behind why an array is good if the GCD of its elements is 1 comes from Bezout's Identity. It states that for any non-zero integers \(a\) and \(b\), if \(d\) is their greatest common divisor, then there exist integers \(x\) and \(y\) such that \(ax + by = d\). If \(d = 1\), then we can say that \(1\) can be expressed as a linear combination of \(a\) and \(b\), and thus, we can get \(1\) using operations on elements of the array.

# ### Implementing GCD Calculation

# First, let's manually implement a function to calculate the GCD of two numbers, which is a foundational step since we won't be using Python's built-in `math.gcd` function:

# ```python
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
# ```

# This function uses the Euclidean algorithm to find the GCD of two numbers, \(a\) and \(b\). The algorithm repeatedly replaces the larger number with the remainder of the larger number divided by the smaller number, until the remainder is 0. The last non-zero remainder is the GCD of the original two numbers.

# ### Solution Without Using Built-in Functions

# Now, let's integrate this understanding into our `Solution` class without using the built-in `gcd` function:

# ```python
# class Solution:
#     def isGoodArray(self, nums: List[int]) -> bool:
#         # Start with the GCD as the first element of the array
#         current_gcd = nums[0]
        
#         # Function to compute GCD, using the Euclidean algorithm
#         def gcd(a, b):
#             while b != 0:
#                 a, b = b, a % b
#             return a
        
#         # Iterate through the array to compute the GCD of all elements
#         for num in nums[1:]:
#             current_gcd = gcd(current_gcd, num)
            
#             # If at any point the GCD is 1, the array is good
#             if current_gcd == 1:
#                 return True
        
#         # If after checking all elements, the GCD isn't 1, the array isn't good
#         return False
# ```

# ### How It Works

# The solution iteratively calculates the GCD of the array elements. If at any point the GCD becomes 1, it means any number can be formed from the array, making it "good" by definition. The key is that if you can form 1, you can scale and add to form any other integer, fulfilling the requirement.

# This approach provides a clear, step-by-step logic to solve the problem without relying on Python's built-in functions, offering a deeper understanding of the mathematical principles involved.

        def gcd(a,b):
            while b:
                a,b = b , a %b
            return a
        
        gcd_found = nums[0]


        for i in range(1, len(nums)):
            gcd_found = gcd(gcd_found, nums[i])
            if gcd_found == 1:
                return True
        return gcd_found == 1
        