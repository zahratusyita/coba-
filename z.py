import time

def display_menu():
    print("\n=== Manajemen Keuangan Pribadi ===")
    print("1. Tambah Transaksi")
    print("2. Tampilkan Semua Transaksi")
    print("3. Hitung Total Pengeluaran dan Pemasukan")
    print("4. Cari Transaksi Tertinggi dan Terendah")
    print("5. Hitung Saldo Akhir")
    print("6. Keluar")

def add_transaction(transactions):
    try:
        amount = float(input("Masukkan jumlah transaksi: "))  
        type_transaction = input("Jenis transaksi (masuk/keluar): ").strip().lower()
        
        if type_transaction not in ['masuk', 'keluar']:
            print("Jenis transaksi tidak valid. Gunakan 'masuk' atau 'keluar'.")
            return
        
        transactions.append({'amount': amount, 'type': type_transaction, 'time': time.strftime('%Y-%m-%d %H:%M:%S')})
        print("Transaksi berhasil ditambahkan!")
    except ValueError:
        print("Harap masukkan angka yang valid!")

def display_transactions(transactions):
    if transactions:
        print("\nRiwayat Transaksi:")
        for i, transaction in enumerate(transactions, 1):
            print(f"{i}. {transaction['time']} - {transaction['type'].capitalize()} - Rp{transaction['amount']:.2f}")
    else:
        print("Belum ada transaksi.")

def calculate_totals(transactions):
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'masuk')
    total_expense = sum(t['amount'] for t in transactions if t['type'] == 'keluar')
    print(f"Total Pemasukan: Rp{total_income:.2f}")
    print(f"Total Pengeluaran: Rp{total_expense:.2f}")

def find_highest_lowest(transactions):
    if transactions:
        highest = max(transactions, key=lambda t: t['amount'])
        lowest = min(transactions, key=lambda t: t['amount'])
        print(f"Transaksi Tertinggi: {highest['type'].capitalize()} - Rp{highest['amount']:.2f} pada {highest['time']}")
        print(f"Transaksi Terendah: {lowest['type'].capitalize()} - Rp{lowest['amount']:.2f} pada {lowest['time']}")
    else:
        print("Tidak ada transaksi untuk dianalisis.")

def calculate_balance(transactions):
    balance = sum(t['amount'] if t['type'] == 'masuk' else -t['amount'] for t in transactions)
    print(f"Saldo Akhir: Rp{balance:.2f}")

def main():
    transactions = []  # List untuk menyimpan transaksi
    while True:
        display_menu()
        choice = input("Pilih menu (1-6): ")
        
        if choice == '1':
            add_transaction(transactions)
        elif choice == '2':
            display_transactions(transactions)
        elif choice == '3':
            calculate_totals(transactions)
        elif choice == '4':
            find_highest_lowest(transactions)
        elif choice == '5':
            calculate_balance(transactions)
        elif choice == '6':
            print("Terima kasih telah menggunakan aplikasi manajemen keuangan. Keluar...")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if _name_ == "_main_":
    main()
