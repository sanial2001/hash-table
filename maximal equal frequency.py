'''
Here's some examples of the cases given where we can delete to make it valid:

    All numbers have a frequency of 1: maxF == 1. In this case, we can choose any of the numbers to delete and will have a valid array where all remaining numbers still occur 1 time:

    2 3 4 5
          ^
    Counts   Freq
    ------   ----
    2: 1     1: 4 {2,3,4,5}
    3: 1
    4: 1
    5: 1

    Set size: 4 {2,3,4,5}
    Max count: 1 --> freq[max]=4.

    We know that all numbers have occured one time since the max freq is still 1. Another way of looking at it would be to see that freq[1]=4 == setsize=4 . We have a satisfactory array of length 4 because we can delete any number and the remaining 3 numbers in set will all have a count of 1.

    One number has a single frequency, and the rest have occured max frequency times: maxF*freq[maxF]==i. In this case we can delete the single occurence to make it valid.

    4 4 5 5 6 7 7
                ^
    Counts   Freq
    ------   ----
    4: 2     1: 1 {6}
    5: 2     2: 3 {4,5,7}
    6: 1
    7: 2

    i: 6 and total numbers seen is i+1=7
    Set size: 4 {4,5,6,7}
    Max count: 2 --> 4,5,7 have occured twice, freq[max]=3
    Single freq: 1 --> 6 only occurs once, freq[1]=1
    max * freq[max] = 2 * 3 = 6 = 7 numbers - 1 deletion

    Delete the single occurence (6) to create a valid array where all numbers of occured the max count (2) times.

    Exactly one number has the max count, and the rest have one less than the max count: (maxF-1)*(freq[maxF-1]+1) ==i . We can delete one occurence of the number with the max count to make all occurences equal at max minus one.

    4 4 5 5 5 6 6
                ^
    Counts   Freq
    ------   ----
    4: 2     1: 0
    5: 3     2: 2 {4,6}
    6: 2     3: 1 {5}

    i: 6 and total numbers seen is i+1=7
    Set size: 3 {4,5,6}.
    Max count: 3 --> Only 5 occurs 3 times, freq[max]=1
    Max count minus one: 2 --> 4 and 6 have occurred twice, freq[max-1]=2
    (max-1)*(freq[max-1]+1) = 2*(2+1)=6.

    Delete one occurence of the number accounting for max freq (5) to create a valid array of length 7.

Alternatively, you could check each case by set size at the cost of terseness and multiple conditions, included just for a more explicit view of each case:

    freq[1] == len(cnt)
    freq[maxF]+freq[1] == len(cnt) and freq[1] == 1
    freq[maxF]+freq[maxF-1] == len(cnt) and freq[maxF] == 1

Here's the same code as above broken out with comments:
'''
import collections
from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        cnt, freq, maxfreq, ans = collections.defaultdict(int), collections.defaultdict(int), 0, 0
        for i, num in enumerate(nums):
            cnt[num] = cnt.get(num, 0) + 1
            freq[cnt[num]] += 1
            freq[cnt[num] - 1] -= 1
            maxfreq = max(maxfreq, cnt[num])
            if maxfreq == 1:
                ans = i + 1
            elif maxfreq * freq[maxfreq] == i:
                ans = i + 1
            elif (maxfreq - 1) * (freq[maxfreq - 1] + 1) == i:
                ans = i + 1
        return ans
