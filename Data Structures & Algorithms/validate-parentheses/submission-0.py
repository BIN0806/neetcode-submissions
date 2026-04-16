class Solution:
    def isValid(self, s: str) -> bool:
        open_dic = { "(": ")", "{":"}", "[":"]"}
        close_dic = { ")": "(", "}":"{", "]":"["}

        stack = []
        for char in s:
            if stack:
                if char in close and stack[-1] == close[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
