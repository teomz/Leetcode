class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append('0')

        l,r= 0,1
        count = 1
        index= 0

        if len(chars) < 2:
            return 1
        
        while r<len(chars):
            if chars[l] == chars[r]:
                r+=1
                count+=1
            else:
                chars[index] = chars[l]
                index+=1
                if count > 1:
                    for i in str(count):
                        chars[index] = i
                        index+=1
                
                count = 1
                l = r
                r+=1

        return index

                
                


                

            


        