class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max_candy = max(candies)

        arr = [False] * len(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy:
                arr[i] = True

        return arr

        