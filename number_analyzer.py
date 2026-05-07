def analyze_number(n):
    # Node 1: Inisialisasi list hasil
    result = []
    
    # Node 1 (lanjutan): Cek Positif
    if n > 0:
        # Node 2
        result.append("Positif")
    # Node 3: Cek Negatif
    elif n < 0:
        # Node 4
        result.append("Negatif")
    else:
        # Node 5
        result.append("Nol")
        
    # Node 6: Cek Genap/Ganjil
    if n % 2 == 0:
        # Node 7
        result.append("Genap")
    else:
        # Node 8
        result.append("Ganjil")
        
    # Node 9: Cek Prima (Tahap 1: Kurang dari sama dengan 1)
    is_prime = True
    if n <= 1:
        # Node 10
        is_prime = False
    else:
        # Node 11: Inisialisasi pembagi (loop condition)
        i = 2
        while i * i <= n:
            # Node 12: Cek sisa bagi
            if n % i == 0:
                # Node 13: Ditemukan pembagi, bukan prima -> keluar loop
                is_prime = False
                break
            # Node 14: Increment pembagi
            i += 1
            
    # Node 15: Evaluasi hasil pengecekan prima
    if is_prime:
        # Node 16
        result.append("Prima")
    else:
        # Node 17
        result.append("Bukan Prima")
        
    # Node 18: Kembalikan hasil
    return result

if __name__ == "__main__":
    # Test cases berdasarkan Independent Paths
    print("n = 0  ->", analyze_number(0))
    print("n = -3 ->", analyze_number(-3))
    print("n = -2 ->", analyze_number(-2))
    print("n = 1  ->", analyze_number(1))
    print("n = 2  ->", analyze_number(2))
    print("n = 3  ->", analyze_number(3))
    print("n = 4  ->", analyze_number(4))
    print("n = 5  ->", analyze_number(5))
