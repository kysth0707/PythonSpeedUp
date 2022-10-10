import timeit
from ShowModule import ShowResult

def For(n = 10000000):
	Sum = 0
	for i in range(n):
		Sum += 1
	return Sum

def While(n = 10000000):
	i = 0
	Sum = 0
	while i < n:
		Sum += i
		i += 1
	return Sum



def main():
	print("> loop")
	ForTime = timeit.timeit(For, number=1)
	WhileTime = timeit.timeit(While, number=1)

	ShowResult(["for", "while"], [ForTime, WhileTime])

if __name__ == "__main__":
	main()