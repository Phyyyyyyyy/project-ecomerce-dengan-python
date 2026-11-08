from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import mysql.connector

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'ecomerce_db'
)
cursor = db.cursor()
cursor.execute("SELECT id_key, jumlah FROM database_stok")
database_stok = {
    nama_barang: jumlah
    for nama_barang, jumlah in cursor.fetchall()
}
cursor.close()

def restock(barang_restock, jumlah_restock):
    barang_restock = barang_restock.capitalize()
    
    if barang_restock in database_stok:
        database_stok[barang_restock] += jumlah_restock

    else:
        database_stok.update({barang_restock:jumlah_restock})
        
    return f"Berhasil di restock"
        
def buat_pesanan(barang_pesanan, jumlah_pesanan):
    
    barang_pesanan = barang_pesanan.capitalize()
    
    if barang_pesanan not in database_stok:
        return
        print(f"Barang '{barang_pesanan}' ngga ditemukan di sistem.")
    
    stok_tersedia = database_stok[barang_pesanan]
    if stok_tersedia < jumlah_pesanan:
        return f"GAGAL: Stok '{barang_pesanan}' ngga cukup. Sisa stok kita cuma: {stok_tersedia}."
    
    database_stok[barang_pesanan] -= jumlah_pesanan
    
    return (
        f"barang {barang_pesanan} unit '{barang_pesanan}' udah dibeli. "
        f"Sisa stok : {database_stok[barang_pesanan]}"
    )

def cek_stok():
    return database_stok

# Inisialisasi Server
with SimpleXMLRPCServer(("192.168.1.5", 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    
    # Daftarkan fungsi agar bisa diakses oleh Client
    server.register_function(buat_pesanan, 'buat_pesanan')
    server.register_function(restock, 'restock')
    server.register_function(cek_stok, 'cek_stok')
    
    print(" [SERVER KELOMPOK 3] Server XML-RPC berjalan di http://localhost:8000/RPC2 ...")
    print("Tekan Ctrl+C untuk berhenti.")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer dimatikan.")