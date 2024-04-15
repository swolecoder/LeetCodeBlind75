class Solution:
    def maximumSwap(self, num: int) -> int:

        data = [int(n) for n in str(num)]
        print(data)
        hashmap = {}

        for index, num in enumerate(data):
            hashmap[num] = index
        print(hashmap)


        for indx, n in enumerate(data):
            for i in range(9, n,-1):
                if i in hashmap and hashmap[i] > indx:
                    data[indx] ,  data[hashmap[i]]=  data[hashmap[i]], data[indx] 
                    # data[hashmap[i]] = n 
                    print(data)
                    return int(''.join(map(str,data)))
                   

        return int(''.join(map(str,data)))
        