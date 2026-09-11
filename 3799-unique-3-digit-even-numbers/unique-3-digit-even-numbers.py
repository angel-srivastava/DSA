class Solution:
    def totalNumbers(self, digits):
        #Angel
        
        freq = Counter(digits)
        ans = set()

        for a in range(1, 10):
            for b in range(10):
                for c in range(0, 10, 2):

                    need = Counter([a, b, c])

                    if all(need[d] <= freq[d] for d in need):
                        ans.add(100*a + 10*b + c)

        return len(ans) 