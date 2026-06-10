class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        if needle == haystack:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            print(haystack[i : i + len(needle)])
            if needle == haystack[i : i + len(needle)]:
                return i
        return -1


haystack = "abc"
needle = "c"

s = Solution()

print(s.strStr(haystack, needle))
