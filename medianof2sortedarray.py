class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1) 
        len2 = len(nums2)
        A,B = nums1,nums2
        if len1>len2:
            A,B=B,A #A will always the smallest length array
        total = len1+len2
        half = total//2
        print("th total is ",total)
        left,right = 0,len(A)-1
        while(True):
            i = (left+right)//2
            print(i)
            j = half-i-2
            print(j)
            Aleft = A[i] if i>=0 else float("-inf")
            Aright = A[i+1] if i+1<len(A) else float("inf")
            Bleft = B[j] if j>=0 else float("-inf")
            Bright = B[j+1] if j+1<len(B) else float("inf")
            print(Aleft,Aright,Bleft,Bright)
            if Aleft<=Bright and Bleft<=Aright:
                if total%2: #if there is a reminder, means it is odd 
                    print('inside even and total%2  is ', total%2)
                    return min(Aright,Bright)
                else:
                    print('inside odd')
                    return 0.5*(max(Aleft,Bleft)+min(Aright,Bright))
            elif Bleft>Aright:
                left+=1
            else:
                right-=1
            
       


