import pandas as pd
 
#text = "De Tweede Wereldoorlog was de escalatie van de Tweede Chinees-Japanse Oorlog die begon in 1937 en een Europese oorlog begonnen in 1939 tot een militair conflict dat van 1941 tot 1945 op wereldschaal werd uitgevochten tussen twee allianties: de asmogendheden en de geallieerden. In het westen worden meestal de jaren 1939 en 1945 aangehouden als begin en eind van de oorlog."

with open('ww2.txt', 'r', encoding= "utf-8") as file:
  text = file.read()

text = text.lower()

l = "qwertyuiopasdfghjklzxcvbnm -áéíóúàèëïöü"
 
for letter in text:
	if letter not in l:
		text = text.replace(letter,'')
 
words = text.split()
twoWords = [words[i] + " " + words[i + 1] for i in range(len(words) - 1)]


dc = {}
 
for twoWord in twoWords:
	if twoWord in dc:
		dc[twoWord] += 1
	else:
		dc.update({twoWord: 1})
 
ndc = sorted(dc.items(), key=lambda x:x[1], reverse = True)
print(ndc)

with open("words2.txt", 'w') as f:  
    for key, value in dc.items():  
        f.write('%s:%s\n' % (key, value))
f.close()
