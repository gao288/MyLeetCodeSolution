class Solution:
    def primePalindrome(self, N):
        while True:
            N = self.generate_next_palindrome(N)
            if self.is_Prime(N):
                return N
            else:
                N += 1


    def is_Prime(self,n):
        if n < 2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False

        return True

        
    def generate_next_palindrome(self,n):
        str_n = str(n)
        i = 0
        j = len(str_n) - 1
        while(i < j):
            if str_n[i] < str_n[j]:
                str_n = str(int(str_n) + 10**(len(str_n)-j) - int(str_n[j])*10**(len(str_n)-j-1))
            elif str_n[i] >= str_n[j]:
                str_n = str_n[:j] + str_n[i] + str_n[j+1:]
                i += 1
                j -= 1

        return int(str_n)

       

s = Solution()
print(s.primePalindrome(9989900))
