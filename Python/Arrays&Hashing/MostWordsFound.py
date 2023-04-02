class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(i.split(" ")) for i in sentences])
