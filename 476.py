class Solution:
    def findComplement(self, num: int) -> int:
        if num == 1:
            return 0
        elif num == 0:
            return 1
        else:
            x = bin(num)[2:]
            y = list(x)
            z=[]
            for c in range(len(y)):
                if y[c]=='1':
                    z.append('0')
                elif y[c]=='0':
                    z.append('1')
            str1 = ''
            for i in z:
                str1+=i
            return (int(str1, 2))


"""
Approach:
x= '101'
y =list(x)# ['1','0','1']
z= ['0','1','0']
str1 = ''
str1='010'
int(binary[2:]#without 0b,2 )

"""