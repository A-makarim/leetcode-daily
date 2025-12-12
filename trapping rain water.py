class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1 
        water = 0

        #key issues resovled
        # while loop had left<= right. it right never changes, LEFT can move uptill right and increase in the loop

        while left < right:
            print("looping")
            if height[left] <= height[right]:
                print("1 if")
                left +=1
                print(height[:left])
                print(left)
                temp = - height[left] + max(height[:left] , default=0) 
                print("temp", temp)
                if temp> 0:
                    water += temp
                print(water)


            else:
                print("else")
                right -=1
                temp = - height[right] + max(height[right +1:], default = 0)
                print("temp", temp)
                if temp> 0:
                    water += temp
                print(water)

        return water




            
         
