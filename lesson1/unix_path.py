class Solution:
    def simplifyPath(self, path: str) -> str:
        path_parts = path.split('/')
        stack = []

        for x in path_parts:
            match (x):
                case '.':
                    continue
                case '..':
                    if len(stack) > 0:
                        stack.pop()
                case '':
                    continue
                case _:
                    stack.append(x)
        return f"/{'/'.join(stack)}" 
    
print(Solution().simplifyPath("/.../a/../b/c/../d/./"))
