# 產生一個雖機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小

import random # random模組
# 讓USER決定猜數字範圍8~11
start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end) # random模組裡面的函式
count = 0 #記數器
while True: # while True無限迴圈 要有break停止
    count += 1 #顯示一邊猜一邊顯示次數
    num = input('請猜數字: ') #input會強制存成字串
    num = int(num) #casting(型別轉換)
    if num == r:
    	print('你猜中了')
    	print('你猜第', count, '次')
    	break
    elif num > r:
    	print('比答案大')
    elif num < r:
    	print('比答案小') # 14~20行是一個if架構
    print('你猜第', count, '次') #這樣可以不用寫三次在if架構裡面

