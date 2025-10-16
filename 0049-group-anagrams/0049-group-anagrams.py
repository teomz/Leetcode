class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        output = []

        for i in strs:
            index = ''.join(sorted(list(i)))
            if index in hashmap:
                hashmap[index] = hashmap[index] + [i]

            else:
                hashmap[index] = [i]
        

        return list(hashmap.values())
        