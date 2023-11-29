class Solution:
    def hammingWeight(self, n):
        self.n = n
        chunk = bin(n)
        hamming = chunk.count('1')
        return(hamming)


