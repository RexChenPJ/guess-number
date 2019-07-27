import random

r = random.randint(1,100) #正確答案

while True:
	i = input ('請輸入1到100其中一個數字: ') #使用者輸入數字
	i = int(i)
	if i > r:
		print('數字再小一點!')
	elif i < r:
		print('數字再大一點!')
	elif i == r:
		print('終於猜對了!!')
		break