awal = int(input("Masukan Nilai Awal : "))
akhir = int(input("Masukan Nilai Akhir : "))
for x in range(awal,akhir):
    if x%9==0:
        continue
    if x%11==0:
        continue
    if x%2==0:

        print (x)
        
            
