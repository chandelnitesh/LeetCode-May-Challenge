class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        arr=list()
        count=0
        size=len(trust)
        if N==1:
            return 1
        if size==1:
            return trust[0][1]
        if size<N:
            size1=N
        else:
            size1=size
        for i in range(size1+1):            
            arr.append(0)
        for i in range(0,size):
            val=trust[i][1]
            #print(val)
            arr[val]=arr[val]+1
        for i in range(0,size):
            val=trust[i][0]
            if arr[val]>0:
                arr[val]-=1
        print(arr)
        N=N-1
        size=len(arr)
        for i in range(size):
            if arr[i]==N:
                res=i
                count+=1
        if count==1:
            return res
        else:
            return -1
        