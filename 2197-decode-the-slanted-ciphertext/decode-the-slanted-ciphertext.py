class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        s=encodedText
        if not s:
            return s

        cols = math.ceil(len(s) / rows)
        res = []

        for start in range(cols):
            r, c = 0, start
            while r < rows and c < cols:
                res.append(s[r * cols + c])
                r += 1
                c += 1

        return ''.join(res).rstrip()