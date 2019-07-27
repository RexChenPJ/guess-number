#產生一個隨機整數1~100(不要印出來)
#讓使用者重複輸入數字去猜
#猜對的話 印出"終於猜對了!"
#猜錯的話 印出"比答案再大/小"
#印出猜了幾次

import random

print('請決定數字範圍: ')
start = int(input('數字範圍開始值: '))
end = int(input ('數字範圍結束值: '))

r = random.randint(start,end) #正確答案
x = 0

while True:
	i = input ('請輸入1到100其中一個數字: ') #使用者輸入數字
	i = int(i)

	if i > r:
		x += 1
		print('數字再小一點!')
	elif i < r:
		print('數字再大一點!')
		x += 1
	elif i == r:
		x += 1
		print('終於猜對了!!您總共猜了', x ,'次。')
		break
	print('您猜了', x ,'次。')
