class Solution:
    def sortSentence(self, s: str) -> str:
        temp= s.split()
        word={}
        final=''
        for i in temp:
            word[i[-1]]= i[:-1]
        for i in sorted(word):
            final=final+''.join(word[i])+' '
        final=final[:-1]
        return final