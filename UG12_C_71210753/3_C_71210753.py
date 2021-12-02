kata='pisang'

for i in range (0,len(kata)+1):
	for j in range(0,i):
		print('  ',kata[j],end='')
	print('\n')
for i in range (len(kata)-1,0,-1):
	for j in range(0,i):
		print('  ',kata[j],end='')
	print('\n')
