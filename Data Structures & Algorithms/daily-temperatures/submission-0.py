class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        days_to_be_warm = [] # (temp, idx)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            print(days_to_be_warm)
            while days_to_be_warm and days_to_be_warm[-1][0] < temp:
                result[days_to_be_warm[-1][1]] = i-days_to_be_warm[-1][1]
                days_to_be_warm.pop()
            print((temp, i))
            days_to_be_warm.append((temp, i))

        return result