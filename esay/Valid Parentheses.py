class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = {'(', '[', '{'}
        closing_brackets = {')': '(', ']': '[', '}': '{'}

        for bracket in s:
            if bracket in opening_brackets:
                stack.append(bracket)
            elif bracket in closing_brackets:
                if not stack or stack.pop() != closing_brackets[bracket]:
                    return False
        return not stack


if __name__ == "__main__":
        solution = Solution()
        s = "[]"
        print(solution.isValid(s))