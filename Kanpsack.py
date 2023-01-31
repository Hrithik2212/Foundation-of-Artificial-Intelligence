
def knapsack(W:int,profit:list,wt:list,n:int)->int:
  if (W == 0 or n==0):
    return 0;
  
  if(wt[n-1]>W):
    return knapsack(W,profit,wt,n-1)
  else:
    return max(profit[n-1]+knapsack(W-wt[n-1],profit,wt,n-1),
                knapsack(W,profit,wt,n-1))
    
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapsack(W, val,wt, n))

"""
OUTPUT
220
"""
