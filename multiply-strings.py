class Solution:
    def multiply(self, num1, num2):
        n1 = [10**i * int(digit) for i, digit in enumerate(num1[::-1])]
        n2 = [10**i * int(digit) for i, digit in enumerate(num2[::-1])]

        sum = 0
        for i in n1:
            for j in n2:
                sum += i*j

        return str(sum)
