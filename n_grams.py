import re

def n_grams(folder_path: str, file_name: str, delimeters: str, alphabet: str):
	with open(f'{folder_path}/{file_name}', 'r', encoding= "utf-8") as file:
		text = file.read()

	text = text.lower()

	l = alphabet + delimeters

	for letter in text:
		if letter not in l:
			text = text.replace(letter,'')
	
	separators = ""
	for delimeter in delimeters:
		separators += delimeter + '|'
	separators = separators[:-1]
	
	words = re.split(separators, text)
	
	twoWords = [words[i] + " " + words[i + 1] for i in range(len(words) - 1)]
	threeWords = [words[i] + " " + words[i + 1] + " " + words[i + 2] for i in range(len(words) - 2)]
	fourWords = [words[i] + " " + words[i + 1] + " " + words[i + 2] + " " + words[i + 3] for i in range(len(words) - 3)]
	fiveWords = [words[i] + " " + words[i + 1] + " " + words[i + 2] + " " + words[i + 3] + " " + words[i + 4] for i in range(len(words) - 4)]
	nWords = [words, twoWords, threeWords, fourWords, fiveWords]

	twd = {}
	for i in range(len(nWords)):
		dc = {}
	
		for iWord in nWords[i]:
			if iWord in dc:
				dc[iWord] += 1
			else:
				dc.update({iWord: 1})

		if i == 1:
			twd = dc

		ndc = sorted(dc.items(), key=lambda x:x[1], reverse = True)

		with open(f"{folder_path}/words{i+1}.txt", 'w') as f:  
			first = True
			for key, value in dc.items():  
				if not first:
					f.write('%s:%s\n' % (key, value))
				else:
					first = False
		f.close()

	#digram będzie multigrafem, czyli wiele krawędzi między dwoma wierzchołkami
	digram = {}

	for word in words:
		if not word in digram:
			digram.update({word+"_left": 0})
			digram.update({word+"_right": 0})

	for twoWord in twd.keys():
		tww = re.split(separators, twoWord)
		digram[tww[0]+"_left"] += twd[twoWord]
		digram[tww[1]+"_right"] += twd[twoWord]