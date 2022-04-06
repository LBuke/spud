import os
from random import randint

for i in range(1, 365):
	for j in range(0, randint(1, 55)):
		a = " days ago"
		b = str(i)
		c = b + a
		with open('file.txt', 'a') as file:
			file.write(c)
		os.system('git add .')
		os.system("git commit --date=\"" + c + "\" -m \"dev " + str(j) + "\"")

os.system('git push -u origin main')
