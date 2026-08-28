class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

#Angel 

        n = len(s)
        count = Counter(s)

        odd = [ch for ch in count if count[ch] % 2 == 1]

        if len(odd) > 1:
            return ""

        half = []
        for ch in sorted(count):
            half.extend([ch] * (count[ch] // 2))

        m = len(half)
        middle = odd[0] if odd else ""

        def make_pal(left):
            return left + middle + left[::-1]

        smallest = make_pal(''.join(half))

        if smallest > target:
            return smallest


        target_half = target[:m]

        cnt = Counter(half)

        possible = True

        for ch in target_half:
            if cnt[ch] == 0:
                possible = False
                break
            cnt[ch] -= 1

        if possible:
            candidate = make_pal(target_half)

            if candidate > target:
                return candidate

        for i in range(m - 1, -1, -1):


            cnt = Counter(half)

            valid = True

            for j in range(i):
                ch = target_half[j]

                if cnt[ch] == 0:
                    valid = False
                    break

                cnt[ch] -= 1

            if not valid:
                continue

            bigger = None

            for ch in sorted(cnt):
                if cnt[ch] > 0 and ch > target_half[i]:
                    bigger = ch
                    break

            if bigger is not None:
                cnt[bigger] -= 1

                suffix = []

                for ch in sorted(cnt):
                    suffix.extend([ch] * cnt[ch])

                new_half = target_half[:i] + bigger + ''.join(suffix)

                return make_pal(new_half)

        return ""