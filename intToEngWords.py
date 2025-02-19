class Solution:
    def numberToWords(self, num: int) -> str:
        # T: O(1), S: O(1)
        if num == 0:
            return "Zero"

        # Define mappings for ones, teens, tens, and thousands
        ones = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
        ]
        teens = [
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        thousands = ["", "Thousand", "Million", "Billion"]

        # Function to convert three-digit numbers
        def three_digit_to_words(n):
            if n == 0:
                return ""
            elif n < 10:
                return ones[n]
            elif n < 20:
                return teens[n - 10]
            elif n < 100:
                return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
            else:
                return (
                    ones[n // 100]
                    + " Hundred"
                    + (" " + three_digit_to_words(n % 100) if n % 100 != 0 else "")
                )

        result = []
        for i in range(len(thousands)):  # Process chunks of 3 digits
            if num % 1000 != 0:
                result.append(
                    three_digit_to_words(num % 1000)
                    + (" " + thousands[i] if thousands[i] else "")
                )
            num //= 1000  # Shift to next three-digit chunk

        return " ".join(reversed(result)).strip()
