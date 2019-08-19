#Lottery app
import random
start = eval(input('Please enter the start of the number: '))
end = eval(input('Please enter the end of the number: '))
rge = eval(input('Please enter the amount of random numbers you want:'))
r = random.randint(start, end)
for i in range(rge):
	r = random.randint(start, end)
	print('第', i + 1, '的亂數隨機碼為', r)
	