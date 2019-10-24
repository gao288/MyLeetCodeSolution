class Solution:
    def reverse(self, x: int) -> int:
        temp = x
        if x < 0:
            temp = -temp
        
        ret = 0
        while temp > 0:
            mod, temp = temp % 10, temp//10
            ret= ret*10+mod
        
        neg_limit= -0x80000000
        pos_limit= 0x7fffffff
            
        if(x<0):
            val=-ret&neg_limit
            if(val==neg_limit):
                return -ret
            else:
                return 0
        elif(x==0):
            return x
        else:
            val = ret&pos_limit
            if(val==ret):
                return ret
            else:
                return 0
        