def ShowResult(Texts, Times):
	"""
	Parameters
	----------
	Texts : list (str)
		The name of Time list
	Times : list (number)
		The time of Function times

	Output
	----------
	Texts[0]        Times[0]  \n
	Texts[1]        Times[1]  \n
	...
	(Loop Texts Length)
	"""
	for i in range(len(Texts)):
		print(f"{Texts[i]}\t\t{Times[i]}")