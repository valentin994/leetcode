class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        # shortest_word = min(strs, key=len) maybe faster than set on the zip
        zipped_set_strs = zip(*strs, strict=True)
        for char in zipped_set_strs:
            if len(set(char)) == 1:
                prefix += char[0]
            else:
                break
        return prefix


s = Solution()
print(s.longestCommonPrefix(["test", "tek", "teuple"]))
