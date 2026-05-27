class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        ans=0

        for ch, CH in zip(ascii_lowercase, ascii_uppercase):

            if ch not in word or CH not in word: continue
  
            ans+= word.rfind(ch) < word.find(CH)

        return ans

        # first={}
        # last={}

        # for index,c in enumerate(word):
        #     if c.isupper():
        #         c=c.lower()
        #         if c not in first:
        #             first[c]=index
        #     else:
        #         last[c]=index

        # count=0

        # for c in string.ascii_lowercase:
        #     if c in first and c in last and first[c] > last[c]:
        #         count+=1
        
        # return count