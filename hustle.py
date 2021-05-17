from sys import stdin,stdout
nmbr = lambda: int(input())
lst = lambda: list(map(int, input().split()))
PI=float('inf')
def fn(pos,rem,start):
    if pos==0:
        if rem==1:
            if a[pos]==0:return 0
            return 1
        return PI
    ans=PI
    if a[pos]==start:
        if a[pos]!=0:ans=fn(pos-1,rem,start-1)
        elif rem:
            for next in range(n):
                ans=min(fn(pos-1,rem-1,next),ans)
    else:
        if start != 0:
            ans = 1 + fn(pos - 1, rem, start - 1)
        elif rem:
            for next in range(n):
                ans = min(int(a[pos]!=0) + fn(pos - 1, rem - 1, next), ans)
    return ans

for _ in range(1):#nmbr()):
    n=nmbr()
    a=lst()
    dp=[[[PI for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
    if a[0]==0:
        dp[0][1][0]=0
    else:dp[0][1][0]=1
    for i in range(1,n):
        for j in range(1,1+n):
            for k in range(n):
                if a[i] == k:
                    if a[i] != 0:
                        dp[i][j][k] = dp[i-1][j][k-1]
                    elif j:
                        for next in range(n):
                            dp[i][j][k] = min(dp[i-1][j-1][next], dp[i][j][k])
                else:
                    if k != 0:
                        dp[i][j][k] = 1 + dp[i-1][j][k-1]
                    elif j:
                        for next in range(n):
                            dp[i][j][k] = min(int(a[i] != 0) + dp[i-1][j-1][k], dp[i][j][k])
    for i in range(n):
        ans=PI
        for start in range(n):
            ans=min(ans,dp[n-1][i+1][start])
        print(ans)
