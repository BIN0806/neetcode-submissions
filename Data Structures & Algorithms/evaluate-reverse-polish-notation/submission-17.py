class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+":  lambda a,b: a+b,
                     "-":  lambda a,b: a-b,
                     "*":  lambda a,b: a*b,
                     "/": lambda a,b: int(a / b)}

        cur_numbers = [] # stack
        for token in tokens:
            if token in operators:
                b = cur_numbers.pop()
                a = cur_numbers.pop()
                result = operators[token](a, b)
                cur_numbers.append(result)
                continue
            cur_numbers.append(int(token))

        return cur_numbers[-1] 