# from math import prod

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         out = []
#         pre = 1
#         for i, n in enumerate(nums):
#             prod = n * pre
#             pre = prod
#             out.append(prod)
#         post = 1
#         print(out)
#         l = len(nums)
#         for i , n in enumerate(out):
#             c = l-i-1
#             print(c)
#             if c == 0:
#                 print(post, nums[c-1])
#                 out[c] = post 

#             else:
#                 print(post, nums[c-1])

#                 out[c] = post * out[c-1]
#             post = post * nums[c]
            


#        # for i, n in enumerate(nums):
#         return out
            


class MyDefaultDict:
    def __init__(self, datatype):
        self.datatype = datatype()
        self.data = {}
    def __getitem__(self, key):
        if key not in self.data:
            self.data[key] = self.datatype
        return self.data[key]
    
dictionary = MyDefaultDict(list)
dictionary['a']
print(dictionary['a'])

def ret5():
    return 5

dictionary2 = MyDefaultDict(ret5)
dictionary2['a']
print(dictionary2['a'])