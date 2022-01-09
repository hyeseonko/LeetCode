#### Logic
Let dp[i]=ith answer and dp[0]=0 and K=1
dp[i]=dp[0]xdp[i-1]+dp[1]xdp[i-2]+dp[2]xdp[i-3]+...+ (until i-K=0)