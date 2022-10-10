import timeit
from ShowModule import ShowResult

def For(n = 10000000):
	Data = []
	for i in range(n):
		Data.append(True)
	return Data

def While(n = 10000000):
	Data = []
	i = 0
	while i < n:
		Data.append(True)
		i += 1
	return Data

def OneLineFor(n = 10000000):
	return [True for _ in range(n)]



def main():
	print("> list fill")
	ForTime = timeit.timeit(For, number=1)
	WhileTime = timeit.timeit(While, number=1)
	OneLineForTime = timeit.timeit(OneLineFor, number=1)
	
	ShowResult(["for", "while", "one line for"], [ForTime, WhileTime, OneLineForTime])

if __name__ == "__main__":
	main()