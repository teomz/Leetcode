class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def padword(maxWidth,sentence):
            string = ''
            sen_length = len(sentence)
            if sen_length > 1:
                padlen = maxWidth - sum([len(i) for i in sentence])
                padperword = padlen//(sen_length -1)   
                padextra = padlen%(sen_length - 1)    
                padsentence = [" "*(padperword+(1 if i <= (padextra-1) else 0)) for i in range(sen_length-1)]    
                parts = []
                for i in range(sen_length - 1):
                    parts.append(sentence[i] + padsentence[i])
                parts.append(sentence[-1])
                return "".join(parts)

                

            else:
                string = " ".join(sentence).ljust(maxWidth)
                return string

            
        output = []
        sentence = []
        length = 0

        for word in range(len(words)):
            i = words[word]
            if length+len(i) > maxWidth:
                sen = padword(maxWidth,sentence)
                output.append(sen)
                sentence = []
                length = 0
            sentence.append(i)
            length += (len(i) + 1)

            if word == len(words)-1:
                last_sen = " ".join(sentence)
                output.append(last_sen.ljust(maxWidth))

        
        

        
        return output



        