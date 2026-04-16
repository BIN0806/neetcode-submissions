class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def sgn(n):
            if n >= 0:
                return 1
            else:
                return 0

        def divide(a, b):
            if 0 >= a/b > -1:
                return 0
            return a // b

        operators = {"+":  lambda a,b: a+b,
                     "-":  lambda a,b: a-b,
                     "*":  lambda a,b: a*b,
                     "/": lambda a,b: divide(a, b)}

        def is_number(n):
            try:
                int(n)
                return True
            except ValueError:
                return False

        cur_numbers = [] # stack
        for token in tokens:
            # print(cur_numbers)
            if token in operators:
                if len(cur_numbers) >= 2:
                    b = cur_numbers.pop()
                    a = cur_numbers.pop()
                    result = operators[token](a, b)
                    print(a, token, b ,"=", result)
                    # print("operator:", operators[token], "result:", result)
                    cur_numbers.append(result)
                    continue

            if is_number(token):
                # print("enter:", token)
                cur_numbers.append(int(token))
                continue

        return cur_numbers[-1] if cur_numbers else 0 