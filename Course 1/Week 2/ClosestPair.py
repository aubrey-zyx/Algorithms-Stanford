import random
import numpy as np

class Solution:
    def sort_points(self, points):
        P = []
        for i in points:
            P.append(i)
        Px = self.merge_sort(P, 0)
        Py = self.merge_sort(P, 1)
        return Px, Py

    def closest_pair(self, Px, Py):
        n = len(Px)
        if n == 1:
            return (Px[0], (1000,1000))
        if n == 2:
            return (Px[0], Px[1])
        best = (Px[0], Px[1])
        Qx, Qy = Px[:n//2], Py[:n//2]
        Rx, Ry = Px[n//2:], Py[n//2:]
        p1, q1 = self.closest_pair(Qx, Qy)
        p2, q2 = self.closest_pair(Rx, Ry)
        d1, d2 = self.euclidean(p1, q1), self.euclidean(p2, q2)
        if d1 < d2:
            best = (p1, q1)
            delta = d1
        else:
            best = (p2, q2)
            delta = d2
        better_pair = self.closest_split_pair(Px, Py, delta)
        if better_pair is not None:
            best = better_pair
        return best

    def closest_split_pair(self, Px, Py, delta):
        n = len(Px)
        x_bar = Px[n//2 - 1][0]
        Sy = []
        best = None
        for point in Py:
            if abs(point[0] - x_bar) <= delta:
                Sy.append(point)
        for i in range(len(Sy)):
            for j in range(1, min(8, len(Sy)-i)):
                d = self.euclidean(Sy[i], Sy[i+j])
                if d < delta:
                    delta = d
                    best = (Sy[i], Sy[i+j])
                    split_better = True
        return best

    def merge_sort(self, a, coordinate):
        n = len(a)
        if n == 1:
            return a
        b = self.merge_sort(a[:n//2], coordinate)
        c = self.merge_sort(a[n//2:], coordinate)
        d = []
        i, j = 0, 0
        while i < len(b) and j < len(c):
            if b[i][coordinate] <= c[j][coordinate]:
                d.append(b[i])
                i += 1
            else:
                d.append(c[j])
                j += 1
        if j == len(c):
            d += b[i:]
        else:
            d += c[j:]
        return d

    def euclidean(self, a, b):
        return np.sqrt(np.square(a[0] - b[0]) + np.square(a[1] - b[1]))

    def brute_force(self, points):
        P = []
        for i in points:
            P.append(i)
        if len(P) < 2:
            return P
        distance = 1000
        best = P[0], P[1]
        for i in range(len(P)):
            for j in range(i + 1, len(P)):
                d = self.euclidean(P[i], P[j])
                if d < distance:
                    distance = d
                    best = P[i], P[j]
        return best

points = set((random.uniform(-10,10), random.uniform(-10,10)) for _ in range(1000))
Px, Py = Solution().sort_points(points)
print("Divide and conquer:")
print(Solution().closest_pair(Px, Py))
print("Brute force:")
print(Solution().brute_force(points))