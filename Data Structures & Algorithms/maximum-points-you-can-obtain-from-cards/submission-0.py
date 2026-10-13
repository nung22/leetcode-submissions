class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # track window, minimum, and total
        n = len(cardPoints) # total cards
        total = sum(cardPoints)
        window = sum(cardPoints[:n-k])
        minimum = window
        # iterate through the array
        for right in range(n - k, n):
            # adjust window
            window += cardPoints[right] - cardPoints[right - (n - k)]
            # compare window against minimum
            minimum = min(minimum, window)
        # return total - minimum
        return total - minimum