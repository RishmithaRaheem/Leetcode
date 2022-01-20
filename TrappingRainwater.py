class Solution(object):
    def trap(self, height):
        left_max = 0
        maxes = [0 for i in height]
        for i in range(0,len(height)):
            current_height = height[i]
            maxes[i] = left_max
            left_max = max(left_max,current_height)
        right_max = 0
        print("left maxes are", maxes)
        
        right_maxes = [0 for i in height]
        for i in reversed(range(len(height))):
            current_height = height[i]
            right_maxes[i] = max(right_max,current_height)
            right_max = max(right_max,current_height)
        print('right maxes are', right_maxes)
        
        result_ = [0 for i in height]
        for i in range(0, len(height)):
            minHeight = min(maxes[i], right_maxes[i])
            current_height = height[i]
            if current_height<minHeight:
                result_[i] = minHeight-current_height
            else:
                result_[i] = 0
                
        print("result array is ",result_)
        
        return sum(result_)
        
        """
        :type height: List[int]
        :rtype: int
        """
        
