
data=[]
count=0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		#count += 1
		#if count % 1000 == 0:
			#print(len(data))

#print('檔案讀取完了，總共有',len(data),'筆資料')

total_len = 0
nu = 0
while nu < len(data):
	total_len += len(data[int(nu)])
	nu += 1

#print(len(data[int(0)]))
print(total_len/int(len(data)))

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

#print('留言的平均長度是',sum_len/len(data))