#stary kod, spełnia część założeń, ale następny (n_grams.py) spełnia wszystkie
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