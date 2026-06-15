# Last updated: 6/15/2026, 11:54:19 AM
1class Solution:
2    def reverseBits(self, n: int) -> int:
3        binary = bin(n)[2:]          
4        binary = binary.zfill(32)    
5        binary = binary[::-1]       
6        return int(binary, 2)  