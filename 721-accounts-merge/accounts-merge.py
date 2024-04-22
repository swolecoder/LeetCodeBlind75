from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}


        for account in accounts:
            name, emails = account[0], account[1:]

            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)
                email_to_name[email] = name
        print(graph)
        print(email_to_name)


        res = []
        stack = []
        seen = set()
        
        for key in graph:
            # print("Ashish1", key)
            if key not in seen:
                stack.append(key)
                seen.add(key)
                local= []
                while stack:
                    node = stack.pop()
                    local.append(node)

                    for nei in graph[node]:
                        if nei not in seen:
                            stack.append(nei)
                            seen.add(nei)
                

                res.append([email_to_name[key]] + sorted(local))
        return res 
#N= number pf account , K = max number of emails
#T -> NK * NlogK
#Space Complexity: NlogK

