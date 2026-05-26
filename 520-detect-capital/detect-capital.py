class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        upper = 0
        
        for c in word:
            if c.isupper():
                upper+=1

        return True if upper==0 or upper== len(word) or (upper==1 and word[0].isupper()) else False