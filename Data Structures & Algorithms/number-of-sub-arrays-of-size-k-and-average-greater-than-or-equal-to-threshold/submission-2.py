class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = sum(arr[:k])
        L = 0
        count = 1 if window / k >= threshold else 0
        for R in range(k,len(arr)):
            window -= arr[L]
            window += arr[R]
            if window >= threshold * k:
                count += 1
            L += 1
        return count