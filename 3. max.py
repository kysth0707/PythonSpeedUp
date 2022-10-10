import timeit
from ShowModule import ShowResult

def FuncMax(n = 10000000):
	global List
	return max(List)

def ForMax(n = 10000000):
	global List
	Max = 0
	for i in List:
		if i > Max:
			Max = i
	return Max

def WhileMax(n = 10000000):
	global List
	i = 0
	Max = 0
	while i < n:
		if List[i] > Max:
			Max = List[i]
		i += 1
	return Max


List = []
def main():
	global List
	print("> max")

	SavedList =  [True for _ in range(10000000)]
	List = SavedList
	ValueA = timeit.timeit(FuncMax, number=1)
	List = SavedList
	ValueB = timeit.timeit(ForMax, number=1)
	List = SavedList
	ValueC = timeit.timeit(WhileMax, number=1)
	
	ShowResult(["func max", "for max", "while max"], [ValueA, ValueB, ValueC])

if __name__ == "__main__":
	main()