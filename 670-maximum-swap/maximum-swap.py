class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [ int(n) for n in str(num)]
        print(num)
        hashmap ={val:index for index , val in enumerate(num)}
        print(hashmap)


        for index,val in enumerate(num):
            for n in range(9,val,-1):
                if n in hashmap and hashmap[n] > index:
                    num[index], num[hashmap[n]] = num[hashmap[n]],num[index]

                    return int(''.join(map(str,num)))
        return int(''.join(map(str,num))) 
        