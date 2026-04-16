class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs:
            encoded.append(str(len(string)))
            encoded.append("#")
            encoded.append(string)
        return "".join(encoded)
    # (12#BILLYATETOO123)(5#PLACE)(2#IT)
    def decode(self, s: str) -> List[str]:
        #while first_ptr is a num
            #increase ptr until see a tag
            # then equals the # of iterations until we should see a number 
            # loop and do the same until ptr is not out of bounds
        iterations = []
        decode = []
        while i < len(s):
            while s[i] != '#':
                iterations.append(s[i])
                i += 1
            iterations = int("".join(iterations))

            cur_string = []
            for j in range(iterations):
                cur_string.append(s[i+j+1])
            cur_string = "".join(cur_string)
            decode.append(cur_string)
            i = i + j
        return decode 