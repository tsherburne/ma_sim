from typing import Union
import numpy as np

seed_stream = [774126224, 805584977, 1851887870]


class Choice:
    def __init__(self, count: int):
        self.count = count


class NormDist:
    def __init__(self, mean: float, std: float):
        self.mean = mean
        self.std = std


class PoissonDist:
    def __init__(self, lam: float):
        self.lam = lam


class NumSpec:
    def __init__(self, num: Union[int, float, Choice, NormDist, PoissonDist] = None, stream: int = 0):
        if num is None:
            # set default
            self.num = NormDist(10.0, 1.0)
        else:
            self.num = num
        self.stream = stream
        if type(self.num) != float and type(self.num) != int:
            # create random number generator
            self.rng = np.random.default_rng(seed=seed_stream[self.stream])

    def getValue(self) -> Union[int, float]:
        if type(self.num) == float or type(self.num) == int:
            return self.num
        elif type(self.num) == Choice:
            return self.rng.choice(self.num.count, 1)[0]
        elif type(self.num) == NormDist:
            return round(self.rng.normal(self.num.mean, self.num.std, 1)[0], 3)
        elif type(self.num) == PoissonDist:
            return self.rng.poisson(self.num.lam, 1)[0]
