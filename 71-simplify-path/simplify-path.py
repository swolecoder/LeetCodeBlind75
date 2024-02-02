class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_item = path.split("/")

        for p in path_item:
            if p == "." or p == "":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + '/'.join(stack)
        