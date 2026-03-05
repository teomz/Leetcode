class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l1 = len(flowerbed) 
        i = 0

        while i < l1:
            prev =  i-1 < 0 or  flowerbed[i-1] == 0
            next =  i+1 >= l1 or  flowerbed[i+1] == 0
            if prev and flowerbed[i] == 0 and next:
                flowerbed[i] = 1
                n-=1
                i+=2
            else:
                i+=1

        return n<=0

        