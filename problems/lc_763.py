import functools
from collections import defaultdict
from typing import List


class Solution:



    def partitionLabels(self, S: str) -> List[int]:

        map = defaultdict(list)

        for i in range(len(S)):
            map[S[i]].append(i)


        intervals = []

        for key, item in map.items():

            if not intervals:
                intervals.append([item[0], item[-1]])
                continue

            intervals_temp = []
            for i in range(len(intervals)):
                if item[0] > intervals[i][0] and item[0] < intervals[i][1] and item[-1] > intervals[i][0] and item[-1] < intervals[i][1]:
                    intervals_temp = []
                    break
                elif item[0] < intervals[i][0] and item[-1] < intervals[i][1] and item[-1] > intervals[i][1]:
                    intervals_temp = []
                    intervals[i][0] = item[0]
                    break
                elif item[0] < intervals[i][1] and item[0] > intervals[i][0] and item[-1] > intervals[i][1]:
                    intervals_temp = []
                    intervals[i][1] = item[-1]
                    break
                elif item[0] < intervals[i][0] and item[-1] > intervals[i][1]:
                    intervals[i][0] = item[0]
                    intervals[i][1] = item[-1]
                    intervals_temp= []
                    break
                else:
                    if len(intervals_temp) == 0:
                        intervals_temp.append([item[0], item[-1]])
            intervals = intervals+ intervals_temp



        return[x[-1]- x[0]+1 for x in intervals]



print(Solution().partitionLabels(S = "ababcbacadefegdehijhklij"))

assert Solution().partitionLabels(S = "ababcbacadefegdehijhklij") == [9,7,8]
