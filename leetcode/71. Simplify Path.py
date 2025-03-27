class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        parts = list(filter(lambda x: x != "", parts))
        result = []
        for part in parts:
            if part == ".":
                pass
            elif part == "..":
                if len(result) > 0:
                    result.pop()
            else:
                result.append(part)
        return "/"+"/".join(result)