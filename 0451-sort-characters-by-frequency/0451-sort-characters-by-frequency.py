from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        z=Counter(s)
        zsort=sorted(z.items(), key=lambda x:x[1],reverse=True)
        res=''
        for i in zsort:
            res+=i[0]*i[1]
        return res
        