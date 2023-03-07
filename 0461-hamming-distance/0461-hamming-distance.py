class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dequeX = deque(bin(x)[2:])
        dequeY = deque(bin(y)[2:])

        length = len(dequeX) if len(dequeX) >= len(dequeY) else len(dequeY)
        sum = 0
        for _ in range(length):
            x, y = 0, 0
            if dequeX:
                x = int(dequeX.pop())
            if dequeY:
                y = int(dequeY.pop())
            sum += x ^ y

        return sum
        