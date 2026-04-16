class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_to_speed = {} 
        for p, s in zip(position, speed):
            position_to_speed[p] = s
        # posiition is unique
        # { position ; speed for cars at that position}
    
        stack = sorted(position, reverse=True) # rev order [9,8,7,5,3,2,1]
        count = 0 

        while stack:
            new_stack, fleet = [], False
            while stack[-1] + position_to_speed[stack[-1]] >= target:
                fleet = True
                stack.pop()

            if stack:
                pos = stack.pop()
                old_speed = position_to_speed[pos]

                new_pos = pos + old_speed
                new_stack.append(new_pos)

                if new_pos not in position_to_speed:
                    position_to_speed[new_pos] = old_speed

            if fleet:
                count += 1  

        return count        

        # [4, 1, 0, 7]  -> [0,1,4,7]
        # [6, 3, 1, 8]  -> [1,3,6,8]
        # [8, 5, 2, 9]  -> [2,5,8,9]
        # [10, 7, 3, 10] -> [3,7,10,10]
        # [9, 4] -> [4,9]
        # [10, 5] -> [5,10]
        # [6] -> [6]
        # ..


