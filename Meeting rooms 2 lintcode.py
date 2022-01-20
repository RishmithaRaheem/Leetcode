"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        count = 0
        result = 0
        s = e = 0
        while s < len(intervals):
            
            if start[s] < end[e]:
                s+=1
                count+=1
            else:
                e+=1
                count-=1
            result = max(result, count)

        return result


        # Write your code here
