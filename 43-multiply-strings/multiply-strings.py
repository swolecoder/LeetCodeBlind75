class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if "0" in [num1,num2]:
            return "0"
        res = [0] * (len(num1) + len(num2))

        num1 = list(num1)[::-1]
        num2 = list(num2)[::-1]
        # print(res)
        for i in range(len(num1)):
            for j in range(len(num2)):
                value = int(num1[i]) * int(num2[j])
                value += res[i+j]

                res[i+j+1] += (value) //10
                res[i+j] = (value) %10
        

        data = res[::-1]
        begin = 0
        while begin < len(data) and data[begin] == 0:  # Corrected condition
            begin += 1

        return ''.join(map(str,data[begin:]))

        