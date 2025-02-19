class Solution:
    def calculate(self, s: str) -> int:
        # T: O(n), S: O(n)
        if not s:
            return 0

        s = s.replace(" ", "")  # Remove spaces
        stack = []
        num = 0
        last_op = "+"  # Start with '+' to add the first number

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)  # Build multi-digit numbers

            if (
                char in "+-*/" or i == len(s) - 1
            ):  # Process when we hit an operator or last char
                if last_op == "+":
                    stack.append(num)
                elif last_op == "-":
                    stack.append(-num)
                elif last_op == "*":
                    stack.append(stack.pop() * num)
                elif last_op == "/":
                    stack.append(int(stack.pop() / num))  # Truncate towards zero

                last_op = char  # Update last operator
                num = 0  # Reset number

        return sum(stack)
