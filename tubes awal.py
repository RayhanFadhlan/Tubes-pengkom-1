
def list_film():

    print("Film yang sedang tayang: ")
    print("(1) Black Adam")
    print("(2) Doctor G")
    print("(3) Contorted")
    print("(4) Pamali")
    print("(5) One Piece Film: Red")
    print()
    input("Input 0 untuk kembali: ")


    return

def pembelian():
    global bioskop
    print("(1) Black Adam")
    print("(2) Doctor G")
    print("(3) Contorted")
    print("(4) Pamali")
    print("(5) One Piece Film: Red")
    print()
    print("Pilih judul film yang akan dibeli: ")
    beli =  int(input("Input:"))
    bioskop.append(beli)
    
    return

def mtix():
    global cash
    cond = True
    while(cond):
        print("Pilih input: ")
        print("(1) Cek balance M-TIX")
        print("(2) Top up Saldo M-TIX")
        print("(3) History Saldo M-TIX")
        print("(4) Kembali")

        opt = int(input("Input: \n"))

        if(opt== 1):
            print(f"Balance M-TIX anda saat ini sebesar IDR {cash}")
            print()
        
        if(opt == 2):

            topup = int(input("Masukkan jumlah Top up Saldo M-TIX"))
            cash += topup
            history.append(f"Anda topup sebanyak IDR{topup}.")

        if(opt == 3):
            print("History saldo anda adalah: ")
            print("\n".join(history))

        if(opt == 4):
            cond = False
    
    return

cond = True
stop = False

while(not stop):

    history = []
    film = []
    bioskop = []
    jam = []

    print("Selamat datang di Cinema 22!")
    print()
    print("Masukkan saldo awal M-TIX anda!")
    print()
    
    cash = int(input("Input saldo: "))
    history.append(f"Saldo awal sebanyak IDR {cash}")
    
    while(cond):
        print("Pilih input : ")
        print("(1) List film yang sedang tayang")
        print("(2) Pembelian Tiket ")
        print("(3) Balance dan update saldo M-TIX")
        pilih = int(input("Input: "))
        print()
        if(pilih == 1):
            list_film()
        elif(pilih == 2):
            pembelian()
        elif(pilih == 3):
            mtix()
