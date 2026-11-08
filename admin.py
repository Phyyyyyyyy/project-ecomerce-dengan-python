import xmlrpc.client
import os
import socket

proxy = xmlrpc.client.ServerProxy("http://192.168.1.5:8000/RPC2")

os.system("cls")

def tampilkan_menu():
    print(f"{"-"*5}daftar stock{"-"*5}")
    stok = proxy.cek_stok()
    
    for barang, jumlah in stok.items():
        print(f"- {barang}: {jumlah} unit")
    print("-" * 35)

if __name__ == "__main__":
    print("[Kelompok 3] terhubung sebagai admin")
    
    while True:
        tampilkan_menu()
        print("Barang yang ingin ditambah kan")
        barang = input("barang : ")
        jumlah = int(input("jumlah : "))
        
        print(f"mengirim permintaan mengambah stock barang : {barang}, jumlah : {jumlah}")
        
        hasil = proxy.restock(barang, jumlah)
        
        print("hasil setelah ditambahkan")
        print(f"{hasil}")
        tampilkan_menu()
        
        sudah = input("jika ingin keluar (yes/nah)?")
        if sudah.lower().startswith("y"):
            break