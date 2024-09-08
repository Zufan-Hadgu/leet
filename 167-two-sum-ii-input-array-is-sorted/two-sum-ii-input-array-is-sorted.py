class Solution(object):
    def twoSum(self, numbers, target):
        left = 1
        right = len(numbers)
        list_of_array = []
        while left < right:
            if numbers[left-1] + numbers[right-1] < target:
                left += 1
            elif numbers[left-1] + numbers[right-1] > target: 
                right -= 1
            else:
                list_of_array.append(left)
                list_of_array.append(right)
                break
        return list_of_array
            
      




         
     
        