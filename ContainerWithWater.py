class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height)-1
        maxArea = 0
        
        #idea: if you maximize distance & height, you'll always maximize area. starting at either end of the array and finding next maximum heights closer together. O(n)
        next_start = start+1 #next new starting / endpoint
        next_end = end-1
        while start < end:
            maxArea = max(maxArea, (end-start)*(min(height[end], height[start])))
            while (next_start < len(height) and next_start < end):
                if height[next_start] > min(height[end], height[start]):
                    break
                next_start += 1
            while (next_end >= 0 and next_end > start):
                if height[next_end] > min(height[end], height[start]):
                    break
                next_end -= 1
            if next_start == len(height) or next_end == -1:
                break
            if height[start] < height[end]:
                start = next_start
            else:
                end = next_end
        
        return maxArea
                
