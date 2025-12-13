import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        pattern = r"^[A-Za-z0-9_]+$"
        
        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        mapping = {key: [] for key in order}

        for i in range(len(code)):
            if (
                isActive[i] and
                businessLine[i] in mapping and
                re.fullmatch(pattern, code[i])
            ):
                mapping[businessLine[i]].append(code[i])

        result = []
        for key in order:
            result.extend(sorted(mapping[key]))

        return result
