from collections import Counter

with open('document.txt') as f:
	lines = f.read()

words = lines.split()
words.sort()
count = Counter(words)
top5 = count.most_common(5)



for pair in top5:
	string = ''
	for item in pair:
		item_isInt = isinstance(item, int)
		if(item_isInt):
			string = string + ": " + str(item)
			print(string)
		else:
			string = item
