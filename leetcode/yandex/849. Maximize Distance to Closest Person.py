class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        start = 0
        end = 0
        cur_max = 0
        i = 0
        while i < len(seats):
            if seats[i] == 1:
                if seats[end] == 1 and seats[start] == 1:

                    if (end - start) // 2 > cur_max:
                        cur_max = (end - start) // 2

                else:

                    if (end - start) > cur_max:
                        cur_max = (end - start)

                start = end
            end += 1
            i += 1
        if end - start - 1 > cur_max:
            cur_max = (end - start - 1)
        return cur_max




