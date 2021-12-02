senin=("tidak ada kielas")
selasa=("kelas ke2 matematika teknik","kelas ke4 bhs indo,kelas ke6 pkn")
rabu=("kelas ke1 riset operasi","kelas ke3 sistem operasi,kelas ke 5 praktikum inlan")
kamis=("kelas k1 imk,kelas ke3 logmat","kelas ke4 praktekkom")
jumat=("kelas ke2 sistem basis data","kelas kie4 praktikum sistem basis data,kelas ke6 inlan")

tanya = str(input("hi momo masukan hari: "))

if tanya=='senin':
	hari=senin
	for i in range (0,len(hari)):
		ke = i+1
		pel = hari[i]
		print("kelas ke-%s adalah %s"%(ke,pel))
elif tanya=='selasa':
	hari=selasa
	for i in range (0,len(hari)):
		ke = i+1
		pel = hari[i]
		print("kelas ke-%s adalah %s"%(ke,pel))
elif tanya=='rabu':
	hari=rabu
	for i in range (0,len(hari)):
		ke = i+1
		pel = hari[i]
		print("kelas ke-%s adalah %s"%(ke,pel))
elif tanya=='kamis':
	hari=kamis
	for i in range (0,len(hari)):
		ke = i+1
		pel = hari[i]
		print("kelas ke-%s adalah %s"%(ke,pel))
elif tanya=='jumat':
	hari=jumat
	for i in range (0,len(hari)):
		ke = i+1
		pel = hari[i]
		print("kelas ke-%s adalah %s"%(ke,pel))
else:
	print(hari)
	print('salah hari')
