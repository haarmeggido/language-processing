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
 
dc = {}
 
for word in words:
	if word in dc:
		dc[word] += 1
	else:
		dc.update({word: 1})
 
ndc = sorted(dc.items(), key=lambda x:x[1], reverse = True)

with open("words.txt", 'w') as f:  
    for key, value in dc.items():  
        f.write('%s:%s\n' % (key, value))
f.close()