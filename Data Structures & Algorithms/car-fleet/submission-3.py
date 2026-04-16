class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position_to_speed = {} 
        # for p, s in zip(position, speed):
        #     position_to_speed[p] = s
        # # posiition is unique
        # # { position ; speed for cars at that position}
        # stack = sorted(position, reverse=True) # rev order [9,8,7,5,3,2,1] 
        # count = 0 

        # while stack:
        #     fleet = False
        #     held = []
        #     while stack and (stack[-1] + position_to_speed[stack[-1]]) >= target:
        #         fleet = True
        #         position_to_speed.pop(stack.pop())

        #     while stack:
        #         pos = stack.pop()
        #         if not stack or (stack and stack[-1] != pos):
        #             old_speed = position_to_speed.pop(pos)
        #         else:
        #             old_speed = position_to_speed[pos]
        #         # print("old:", pos, old_speed)
        #         new_pos = pos + old_speed 

        #         held.append(new_pos)
        #         print(held)
        #         if new_pos not in position_to_speed:
        #             # print("new:", new_pos, old_speed)
        #             position_to_speed[new_pos] = old_speed
        #     print(position_to_speed)
        #     count += 1 if fleet else 0
        #     stack = held 
        # return count        

        # [4, 1, 0, 7]  -> [0,1,4,7]
        # [6, 3, 1, 8]  -> [1,3,6,8]
        # [8, 5, 2, 9]  -> [2,5,8,9]
        # [10, 7, 3, 10] -> [3,7,10,10]
        # [9, 4] -> [4,9]
        # [10, 5] -> [5,10]
        # [6] -> [6]
        # ..

        stack = []
        info_arr = []
        for i in range(len(position)):
            info = (position[i], speed[i], (target-position[i])/speed[i])
            info_arr.append(info)
        info_arr.sort(key=lambda x: x[0])

        while info_arr:
            cur_time = info_arr.pop()[2]
            print("cur_time:", cur_time)
            if stack and stack[-1] >= cur_time:
                continue
            stack.append(cur_time)
            print(stack)
        return len(stack)