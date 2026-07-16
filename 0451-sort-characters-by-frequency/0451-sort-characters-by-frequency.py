class Solution:
    def frequencySort(self, s: str) -> str:
        mp={}
        for ch in s:
            if ch not in mp:
                mp[ch]=1
            else:
                mp[ch]+=1
        arr=sorted(mp.items(),key=lambda x:x[1],reverse=True)
        ans=""
        for ch,freq in arr:
            ans+=ch*freq 
        return ans
