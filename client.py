import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://192.168.1.5:8000/RPC2")

def tampilkan_menu_stok():
    print(f"\n{"-"*3}DAFTAR STOK BARANG DI SERVER{"-"*3}")
    stok = proxy.cek_stok()
    
    for barang, jumlah in stok.items():
        print(f"- {barang}: {jumlah} unit")
    print("-" * 35)

if __name__ == "__main__":
    print("[CLIENT KELOMPOK 3] terhubung sebagai pembeli")
    
    while True:
        tampilkan_menu_stok()
        
        barang_dipesan = input("barang \t: ")
        jumlah_dipesan = int(input("jumlah \t: "))
        
        print(f"\njumlah pemesanan {jumlah_dipesan} barang '{barang_dipesan}'...")
        
        hasil = proxy.buat_pesanan(barang_dipesan, jumlah_dipesan)
        
        print("berhasil di beli")
        print(f"{hasil}")
        
        sudah = input("masih ingin lanjut (yes/nah) ?")
        if sudah.lower().startswith("n"):
            break