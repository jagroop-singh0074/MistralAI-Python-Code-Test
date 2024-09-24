class Solution(object):
    def strongPasswordChecker(self, password):
        missing_types = 3
        if any('a' <= c <= 'z' for c in password):
            missing_types -= 1
        if any('A' <= c <= 'Z' for c in password):
            missing_types -= 1
        if any(c.isdigit() for c in password):
            missing_types -= 1

        replace = 0
        one = two = 0
        p = re.sub(r'(.)\1*', r'\1', password)
        for b in [match.group(0) for match in re.finditer(r'(.)\1*', password)]:
            if len(b) < 3:
                continue
            l = len(b)
            replace += l // 3
            if l % 3 == 0:
                one += 1
            elif l % 3 == 1:
                two += 1

        if len(password) > 20:
            delete = len(password) - 20
            if delete <= replace:
                replace -= delete
                return delete + max(missing_types, replace)
            else:
                replace = max(0, replace - (delete - replace))
                return delete + max(missing_types, replace)
        elif len(password) < 6:
            return max(missing_types, 6 - len(password))
        else:
            return max(missing_types, replace)
