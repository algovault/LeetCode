# class Solution:
#     @classmethod
#     def defangIPaddr(self, address) -> str:
#         self.address = address
#         y = "."
#         if (address.find(".")>=1):
#          print("test1")
#          address = address.replace(".", "[.]")
#          print(address)

class Solution:
    @classmethod
    def defangIPaddr(self, address: str) -> str:
        self.address = address
        if (address.find(".")>=1):
         address = address.replace(".", "[.]")
         print(address)

Test = Solution
Test.defangIPaddr("10.0.0.1")
