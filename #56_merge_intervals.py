class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_lst = []
        intervals = sorted(intervals, key=lambda x: x[0])
        for interval in intervals:
            if len(merged_lst) == 0 or merged_lst[-1][1] < interval[0]:
                merged_lst.append(interval)
            else:
                merged_lst[-1][1] = max(merged_lst[-1][1], interval[1])
        return merged_lst