class HNumber:
    def __init__(self,levels):
        self.depth = 0
        self.counts = [0 for x in range(levels)]
        self.number = ""

    def incrementDepth(self):
        self.depth += 1

    def decrementDepth(self):
        self.depth -= 1

    def incrementLevel(self):
        self.counts[self.depth] += 1

    def decrementLevel(self):
        self.counts[self.depth] -= 1

    def asString(self):
        self.number = ""
        for i in range(self.depth + 1):
            self.number += str(self.counts[i])
            if i < self.depth:
                self.number += '_'
        return self.number
