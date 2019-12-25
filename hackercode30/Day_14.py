class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self,):
        self.sortedelement=sorted(self.__elements)
        self.maximumDifference=self.sortedelement[-1]-self.sortedelement[0]
        return self.maximumDifference

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)