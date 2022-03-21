tan = ["Tanaman Cabai Rawit","Tanaman Buah Naga","Tanaman Anggur Tanpa Biji","Pohon Mangga Apel","Pohon Alpukat"
    ,"Pohon Durian Musang King"]

price_tan = [15,25,15,85,70,150]
stock_tan = [5] * 6
height_tan = [40,30,60,100,70,70]

item = ["Media tanam 1 kg","Media tanam 2 kg","Media tanam 5 kg","Pupuk Organik (0,5 kg)","Pot (diameter 30 cm)","Pot (diameter 50 cm)"]
price_item = [15,25,60,15,10,35]
stock_item = [5] * 6

cart_tan = [0]*6
cart_item = [0]*6


def view_stock_tan():
    print("----------------------------------------------------------------")
    print("|                          Tanaman                             |")
    print("----------------------------------------------------------------")

    for i,t in enumerate(tan):
        print(i+1,". ",t,sep="")
        print("Tinggi : ",height_tan[i]," cm",sep=" ")
        print("Harga : Rp",price_tan[i],".000,00/buah",sep="")
        print("Stock : ",stock_tan[i]," buah",sep="")
        print("----------------------------------------------------------------")


def view_stock_item():
    print("----------------------------------------------------------------")
    print("|                   Alat dan perlengkapan                      |")
    print("----------------------------------------------------------------")

    for i, t in enumerate(item):
        print(i + 1, ". ", t, sep="")

        print("Harga : Rp", price_item[i], ".000,00/buah", sep="")
        print("Stock : ", stock_item[i], " buah", sep="")
        print("----------------------------------------------------------------")

def menu_pembeli():
    while (True):
        print("-----------------------------------------")
        print("|             Menu Pembeli              |")
        print("-----------------------------------------")
        print("1. Beli tanaman")
        print("2. Beli alat dan perlengkapan")
        print("3. Kembali ke menu utama\n")

        choice = int(input(">> "))
        if choice == 1:
            while(True):
                view_stock_tan()
                choice = int(input("Beli tanaman no [1-6 | 0 untuk kembali]: "))


                if choice == 0 or choice > 6:
                    break

                qty = int(input("Berapa banyak yang ingin Anda beli ? "))

                choice -= 1

                if qty > stock_tan[choice]:
                    print("Stock tanaman tidak mencukupi")
                    input("Tekan enter untuk lanjut...")
                else:
                    print("Total harga :",qty*price_tan[choice],"k")
                    beli = input("Apakah anda yakin ingin membeli ? [Y/N] : ")
                    if beli == 'Y' or beli == 'y':
                        print(tan[choice],"berhasil di beli !")
                        stock_tan[choice] -= qty;
                        cart_tan[choice] += qty
                        input("Tekan enter untuk lanjut...")
                    else:
                        break

        elif choice == 2:
            while (True):
                view_stock_item()
                choice = int(input("Beli alat no [1-6 | 0 untuk kembali]: "))

                if choice == 0 or choice > 6:
                    break

                qty = int(input("Berapa banyak yang ingin Anda beli ? "))

                choice -= 1

                if qty > stock_item[choice]:
                    print("Stock alat tidak mencukupi")
                    input("Tekan enter untuk lanjut...")
                else:
                    print("Total harga :", qty * price_item[choice], "k")
                    beli = input("Apakah anda yakin ingin membeli ? [Y/N] : ")
                    if beli == 'Y' or beli == 'y':
                        print(item[choice], "berhasil di beli !")
                        stock_item[choice] -= qty;
                        cart_item[choice] += qty
                        input("Tekan enter untuk lanjut...")
                    else:
                        break

        elif choice == 3:
            return



def menu_penjual():
    while(True):
        print("-----------------------------------------")
        print("|             Menu Penjual              |")
        print("-----------------------------------------")
        print("1. Cek stock tanaman")
        print("2. Cek stock alat dan perlengkapan")
        print("3. Hitung total penghasilan")
        print("4. Tambah stock tanaman")
        print("5. Tambah stock alat dan perlengkapan")
        print("6. Kembali ke menu utama\n")

        choice = int(input(">> "))
        if choice == 1:
            view_stock_tan()
            input("Tekan enter untuk lanjut...")
        elif choice == 2:
            view_stock_item()
            input("Tekan enter untuk lanjut...")
        elif choice == 3:
            print("-----------------------------------------")
            print("|              Penghasilan               |")
            print("-----------------------------------------")
            sum = 0
            for i in range(6):
                if cart_tan[i] > 0:
                    print(tan[i], "sebanyak", cart_tan[i], "buah dengan total harga", price_tan[i] * cart_tan[i], "k")
                    sum+= price_tan[i] * cart_tan[i]

            for i in range(6):
                if cart_item[i] > 0:
                    print(item[i], "sebanyak", cart_item[i], "buah dengan total harga", price_item[i] * cart_item[i],
                          "k")
                    sum += price_item[i] * cart_item[i]

            print("\nTotal penghasilan :",sum,"k")
            input("Tekan enter untuk lanjut...")
        elif choice == 4:
            view_stock_tan()
            choice = int(input("Tambah stock tanaman no [1-6|0 untuk kembali]: "))
            if choice == 0 or choice > 6:
                continue

            choice-=1

            if(stock_tan[choice] > 2):
                print("Stock tanaman masih cukup")
                input("Tekan enter untuk lanjut...")
            else:
                stock_tan[choice] += int(input("Berapa banyak yang ingin di tambahkan :"))
                print("Berhasil ditambahkan !")
                input("Tekan enter untuk lanjut...")

        elif choice == 5:
            view_stock_item()
            choice = int(input("Tambah stock alat no [1-6|0 untuk kembali]: "))
            if choice == 0 or choice > 6:
                continue

            choice-=1

            if(stock_item[choice] > 2):
                print("Stock alat masih cukup")
                input("Tekan enter untuk lanjut...")
            else:
                stock_item[choice] += int(input("Berapa banyak yang ingin di tambahkan :"))
                print("Berhasil ditambahkan !")
                input("Tekan enter untuk lanjut...")


        elif choice == 6:
            return




while(True):
    print("--------------------------------------------------")
    print("|     Selamat datang di toko Agria e-mart !      |")
    print("--------------------------------------------------")
    print("1. Enter sebagai penjual")
    print("2. Enter sebagai pembeli")
    print("3. Keluar\n")


    choice = int(input(">> "))
    if choice == 1:
        menu_penjual()
    elif choice == 2:
        menu_pembeli()
    elif choice == 3:
        print("Terima kasih telah menggunakan aplikasi Agria e-mart")
        input("Tekan enter untuk lanjut...")
        quit()
