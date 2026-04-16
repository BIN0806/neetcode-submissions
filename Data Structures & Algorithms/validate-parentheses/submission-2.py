class Solution:
    def isValid(self, s: str) -> bool:
        open_dic = { "(": ")", "{":"}", "[":"]"}
        close_dic = { ")": "(", "}":"{", "]":"["}

        stack = []
        for char in s:
            if stack:
                if char in close_dic and stack[-1] == close_dic[char]:
                    stack.pop()
                elif char in open_dic:
                    stack.append(char)
                else:
                    return False
            else:
                stack.append(char)
        return True if len(stack) == 0 else False