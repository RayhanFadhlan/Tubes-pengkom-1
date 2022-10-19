n = int(input("Penghasilan: "))
bul = int(input("Bulan: "))
pajak = 0
juta = 1000000
if(0<n<50):
    pajak = n*juta*0.05
elif(50<n<250):
    pajak = n*juta*0.15
elif(250<n<500):
    pajak = n*juta*0.25
else:
    pajak = n*juta*0.35

denda = 0
total = 0
if(bul>1):
    denda = (bul-1)*pajak*0.12
    print("tes", denda)
    if(denda>(150*juta)*(bul-1)):
        denda == 150*juta*(bul-1)
        print("tes2", denda)
    total = bul*pajak + denda
else:
    total = bul*pajak
print(int(total))