# class Solution:
#     def hammingWeight(self, n):
#         self.n = n
n = 0b11111111111111111111111111111101
chunk = bin(n)
hamming = chunk.count('1')
print(hamming)


