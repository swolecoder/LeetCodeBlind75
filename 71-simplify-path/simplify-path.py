class Solution:
    def simplifyPath(self, path: str) -> str:
        path_item = path.split("/")
        stack = []
        print(path_item)

        for p in path_item:
            if p == "" or p ==".":
                continue
            elif  p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        print(stack)

        return "/" + '/'.join(stack)
        