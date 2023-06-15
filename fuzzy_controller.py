class FuzzyController:

    def __init__(self):
        pass

    def close_L(self, x):
        if 0 <= x <= 50:
            return -x / 50 + 1
        return 0

    def moderate_L(self, x):
        if 35 <= x <= 50:
            return x / 15 - 7 / 3
        if 50 < x <= 65:
            return -x / 15 + 13 / 3
        return 0

    def far_L(self, x):
        if 50 < x <= 100:
            return x / 50 - 1
        return 0

    def close_R(self, x):
        if 0 <= x <= 50:
            return -x / 50 + 1
        return 0

    def moderate_R(self, x):
        if 35 <= x <= 50:
            return x / 15 - 7 / 3
        if 50 < x <= 65:
            return -x / 15 + 13 / 3
        return 0

    def far_R(self, x):
        if 50 < x <= 100:
            return x / 50 - 1
        return 0

    def rotation_high_right(self, x):
        if -50 <= x <= -20:
            return x / 30 + 5 / 3
        if -20 < x <= -5:
            return -x / 15 - 1 / 3
        return 0

    def rotation_low_right(self, x):
        if -20 <= x <= -10:
            return x / 10 + 2
        if -10 < x <= 0:
            return -x / 10
        return 0

    def rotation_nothing(self, x):
        if -10 <= x <= 0:
            return x / 10 + 1
        if 0 < x <= 10:
            return -x / 10 + 1
        return 0

    def rotation_low_left(self, x):
        if 0 <= x <= 10:
            return x / 10
        if 10 < x <= 20:
            return -x / 10 + 2
        return 0

    def rotation_high_left(self, x):
        if 5 <= x <= 20:
            return x / 15 - 1 / 3
        if 20 < x <= 50:
            return -x / 30 + 5 / 3
        return 0

    def max_rotate(self, i, low_left, low_right, high_right, high_left, nothing):
        result = max(min(self.rotation_low_left(i), low_left)
                     , min(self.rotation_low_right(i), low_right)
                     , min(self.rotation_high_left(i), high_left)
                     , min(self.rotation_high_right(i), high_right)
                     , min(self.rotation_nothing(i), nothing))

        return result

    def linspace(self, start, end, n):
        dif = (end - start) / n
        integ = []
        x = start
        while x < end:
            integ.append(x)
            x = x + dif
        return integ

    def decide(self, left_dist, right_dist):
        """
        main method for doin all the phases and returning the final answer for rotation
        """

        # get memberships for intersections
        low_right = min(self.close_L(left_dist), self.moderate_R(right_dist))
        high_right = min(self.close_L(left_dist), self.far_R(right_dist))
        low_left = min(self.moderate_L(left_dist), self.close_R(right_dist))
        high_left = min(self.far_L(left_dist), self.close_R(right_dist))
        nothing = min(self.moderate_L(left_dist), self.moderate_R(right_dist))

        soorat = 0.0
        makhraj = 0.0
        x = self.linspace(-50, 50, 1000)
        delta = x[1] - x[0]
        for i in x:
            u = self.max_rotate(i, low_left, low_right, high_right, high_left, nothing)
            soorat += u * delta * i
            makhraj += u * delta
        center = 0.0
        if makhraj != 0:
            center = 1.0 * (float(soorat)) / float(makhraj)
        return center
