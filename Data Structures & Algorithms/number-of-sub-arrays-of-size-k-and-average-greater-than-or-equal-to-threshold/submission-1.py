class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = sum(arr[:k])
        L = 0
        count = 0
        for R in range(k,len(arr)):
            if window / k >= threshold:
                count += 1
            window -= arr[L]
            window += arr[R]
            L += 1
        if window / k >= threshold:
            count += 1
        return count