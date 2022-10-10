import timeit
import numpy
from ShowModule import ShowResult

def FuncSum(n = 10000000):
	global List
	return sum(List)

def ForSum(n = 10000000):
	global List
	Sum = 0
	for i in List:
		Sum += i
	return Sum

def WhileSum(n = 10000000):
	global List
	i = 0
	Sum = 0
	while i < n:
		Sum += List[i]
		i += 1
	return Sum

def NumpySumWithArrayConvert(n = 10000000):
	global List
	return numpy.sum(numpy.array(List))

def NumpySumPure(n = 10000000):
	global List
	return numpy.sum(numpy.arange(n))

def MathSum(n = 10000000):
	return (n + 1) * n // 2


List = []
def main():
	global List
	print("> sum test")

	SavedList =  [True for _ in range(10000000)]
	List = SavedList
	ValueA = timeit.timeit(FuncSum, number=1)
	List = SavedList
	ValueB = timeit.timeit(ForSum, number=1)
	List = SavedList
	ValueC = timeit.timeit(WhileSum, number=1)
	List = SavedList
	ValueD = timeit.timeit(NumpySumWithArrayConvert, number=1)
	List = SavedList
	ValueE = timeit.timeit(NumpySumPure, number=1)
	ValueF = timeit.timeit(MathSum, number=1)
	
	ShowResult(["func sum", "for sum", "while sum", "numpy sum with convert", "numpy sum pure", "math sum"], [ValueA, ValueB, ValueC, ValueD, ValueE, ValueF])

if __name__ == "__main__":
	main()