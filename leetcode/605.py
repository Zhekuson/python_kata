class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flower_count = 0
        len_bed = len(flowerbed)
        if len_bed == 1:
            return n + flowerbed[0] < 2
        if flowerbed[0] + flowerbed[1] == 0:
            flowerbed[0] = 1
            flower_count += 1

        for i in range(1, len_bed - 1):
            plot_sum = flowerbed[i - 1] + flowerbed[i] + flowerbed[i + 1]
            if plot_sum == 0:
                flowerbed[i] = 1
                flower_count += 1

        if len_bed > 2 and flowerbed[-2] + flowerbed[-1] == 0:
            flower_count += 1

        return n <= flower_count