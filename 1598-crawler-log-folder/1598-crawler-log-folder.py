class Solution:
    def minOperations(self, logs: List[str]) -> int:
        x=0
        for log in logs:
            if log.endswith("../") and x!=0:
                x-=1
            elif log.endswith("./"):
                x+=0
            else:
                x+=1
        return x