class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        map = Counter(ages)
        print(map)

        def can_send_request(x, y):

            cal = y <= 0.5 * x + 7 or y > x or  (y > 100 and x < 100)

            if cal:
                return False
            else:
                return True

        

        total = 0
        

        for k, v in map.items():

            for k1, v1 in map.items():
                if can_send_request(k,k1):
                    print(k,k1)
                    if k1 == k:
                        total += v1 * (v-1)
                    else:
                        total += v1 * v

        print(total)
        return total 






