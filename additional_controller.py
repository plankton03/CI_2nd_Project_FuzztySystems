class FuzzyGasController:
    """
    # emtiazi todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        pass

    def center_close(self, x):
        if 0 <= x <= 50:
            return -x / 50 + 1
        return 0

    def center_moderate(self, x):
        if 40 <= x <= 50:
            return x / 10 - 4
        if 50 <= x <= 100:
            return -x / 50 + 2
        return 0

    def center_far(self, x):
        if 90 <= x <= 200:
            return x / 110 - 9 / 11
        if x > 200:
            return 1
        return 0

    def gas_low(self, x):
        if 0 <= x <= 5:
            return x / 5
        if 5 < x <= 10:
            return -x / 5 + 1
        return 0

    def gas_medium(self, x):
        if 0 <= x <= 15:
            return x / 15
        if 15 < x <= 30:
            return -x / 15 + 2
        return 0

    def gas_high(self, x):
        if 25 <= x <= 30:
            return x / 5 - 5
        if 30 < x <= 90:
            return -x / 60 + 3 / 2
        return 0

    def max_factor(self, x, low, medium, high):
        result = max(min(self.gas_low(x), low),
                     min(self.gas_medium(x), medium),
                     min(self.gas_high(x), high))
        return result

    def linspace(self, start, end, n):
        dif = (end - start) / n
        integ = []
        x = start
        while x < end:
            integ.append(x)
            x = x + dif
        return integ


    def decide(self, center_dist):
        """
        main method for doin all the phases and returning the final answer for gas
        """
        low = self.center_close(center_dist)
        medium = self.center_moderate(center_dist)
        high = self.center_far(center_dist)

        soorat = 0.0
        makhraj = 0.0
        x = self.linspace(0, 90, 1000)
        delta = x[1] - x[0]
        for i in x:
            u = self.max_factor(i, low, medium, high)
            soorat += u * i * delta
            makhraj += u * delta
        center = 0.0
        if makhraj != 0:
            center = 1.0 * (float(soorat)) / float(makhraj)
        return center
