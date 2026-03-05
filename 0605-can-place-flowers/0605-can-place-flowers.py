class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l1 = len(flowerbed) 
        i = 0

        while i < l1:
            prev = 0 if i-1 < 0 else  flowerbed[i-1]
            next = 0 if i+1 >= l1 else  flowerbed[i+1]
            if prev == flowerbed[i] == next == 0:
                print(i)
                flowerbed[i] = 1
                n-=1
                i+=2
            else:
                i+=1

        return n<=0

        