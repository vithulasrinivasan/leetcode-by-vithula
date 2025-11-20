class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        '''
        Logic used : find the intersection of the intervals
        3 cases
        [start1,end1] [start2,end2]
        
        case 1 : do not overlap
        end1<start2 => start2-end1 > 0 
        select 2 distinct elements from both the intervals = 4

        case 2: overlap edge to edge
        end1==start2 => start2-end1==0
        select 1 common element to both intervals and 1 distinct element from each intervals = 3

        case 3: overlap
        end1>start2 => start2-end1<0
        select 2 elements common to both the intervals = 2

        '''

        intervals.sort(key=lambda x:x[1])
        nums=0
        prev_start , prev_end = -1, -1
        print(intervals)

        for curr_start, curr_end in intervals:
            if prev_start == -1 or prev_end < curr_start: # do not overlap
                nums+=2
                prev_start = curr_end -1
                prev_end = curr_end

            elif prev_start < curr_start: #overlap
                if prev_end !=curr_end:
                    prev_start = prev_end
                    prev_end = curr_end
                else:
                    prev_start = curr_end -1
                    prev_end = curr_end
                nums+=1
        return nums