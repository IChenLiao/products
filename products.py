import os #operating system 作業系統


products = [] #放if外面代表，不管有沒有讀取檔案都要做這個清單
if os.path.isfile('product.csv'): #os這個模組的path小模組的isfile功能
	#可以檢查檔案在不在電腦裡
	print('yeah!')
	with open ('products.csv', 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續，代表直接跳下一回，略過這一回
			#continue跟break一樣只能寫在迴圈裡
			name, price = line.strip().split(',') #strip()代表將換行符號'\n'拿掉
			#split(',')代表看到','就做切割
			products.append([name, price])
	print(products)

else:
	print('找不到檔案...')



#讀取檔案
#products = []
#with open ('products.csv', 'r', encoding = 'utf-8') as f:
		#for line in f:
			#if '商品,價格' in line:
				#continue #繼續，代表直接跳下一回，略過這一回
			#continue跟break一樣只能寫在迴圈裡
			#name, price = line.strip().split(',') #strip()代表將換行符號'\n'拿掉
			#split(',')代表看到','就做切割
			#products.append([name, price])
#print(products)


#讓使用者輸入
#products = []
while True: #未知次數適合用while loop
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price) #型別轉換
	#p = []
	#p.append(name)
	#p.append(price)
	p = [name, price]
	products.append(p)
print(products)

print(products[0][0]) #會印出第1個組合中的name

#印出所有購買紀錄
for p in products:
	#print(p)
	print(p[0], '的價格是', p[1])

#字串可以做加&乘
#'abc' + '123' = 'abc123'cls
#'abc' * 3 = 'abcabcabc'

#寫入檔案
with open ('products.csv', 'w', encoding = 'utf-8-sig') as f: #csv檔可用excel打開
	f.write('商品,價格\n') #沒寫utf-8，excel會無法顯示新寫入的欄位名稱
	for p in products: # for loop
		f.write(p[0] + ',' + str(p[1]) + '\n') #真正寫入 #用逗號分隔excel才會換格 #\n是換行符號
		#加法只能字串跟字串合併，p[1]在前面已轉成整數，因此要在這轉為字串才行 

#最終，這個程式可以讀取現有檔案，也可以在讀取後額外寫入檔案儲存