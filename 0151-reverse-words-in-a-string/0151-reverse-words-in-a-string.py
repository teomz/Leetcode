class Solution:
    def reverseWords(self, s: str) -> str:

        string = []

        word_list = s.split()
        print(word_list)
        for i in range(len(word_list)-1,-1,-1):
            string.append(word_list[i])

        return " ".join(string)
