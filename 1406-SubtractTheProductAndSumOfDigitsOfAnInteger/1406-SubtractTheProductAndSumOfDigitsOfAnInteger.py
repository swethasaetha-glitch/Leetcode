# Last updated: 6/4/2026, 9:42:16 PM
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum1=0
        product=1
        for i in str(n):
            sum1=sum1+int(i)
            product=product*int(i)
        return product-sum1