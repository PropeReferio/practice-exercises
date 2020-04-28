import math

class Solution:
    def get_digit(self, x: int, dig: int) -> int:
        '''Takes an int an a digit as input, outputs the value of said digit.'''
        return x // 10 ** dig % 10
        # First floor division by 10 for 10's place,
        # 100 for 100's place, etc (puts 100's place digit in 1's place)
        # Then get the remainder of division by 10 to get digit's value
        
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        left_dig, right_dig = int(math.log10(x)), 0
        print(left_dig)
        while left_dig > right_dig:
            if self.get_digit(x, left_dig) != self.get_digit(x, right_dig):
                return False
            left_dig -= 1
            right_dig += 1
        return True