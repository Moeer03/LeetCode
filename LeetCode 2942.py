class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        r = []
        for i,j in enumerate(words):
            if x in j:
                r.append(i)
        return r
