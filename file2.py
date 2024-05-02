# import file

# program sederhana 

file = open("data.txt", "a+")

def tambahkan_ke_list(data):
    file.write('\n' + data)
    tanya_user()

def tanya_user():
    pilihan = input("apa yang ingin kamu lakukan: 1. tambah data, 2. lihat data, 3. keluar")
    if pilihan == "1":
        tambahkan_ke_list(input("masukkan data yang ingin ditambahkan: "))
    elif pilihan == "2":
        print(file.read())
    elif pilihan == "3":
        exit()
    else:
        print("pilihan tidak valid")

tanya_user()
