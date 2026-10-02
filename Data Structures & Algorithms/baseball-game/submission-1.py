class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stake = []

        for operation in operations:
            if operation == "C":
                stake.pop()
            elif operation == "D":
                stake.append(stake[-1] * 2)
            elif operation == "+":
                stake.append(stake[-1] + stake[-2])
            else:
                stake.append(int(operation))

        return sum(stake)
        