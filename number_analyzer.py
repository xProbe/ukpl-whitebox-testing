def analyze_number(n):
    # list hasil
    result = []
    
    # node 1, untuk cek postitif gak
    if n > 0:
        # node 2, hasilnya
        result.append("Positif")
    # node 3, untuk cek negatif gak
    elif n < 0:
        # node 4, hasilnya
        result.append("Negatif")
    else:
        # node 5, hasilnya
        result.append("Nol")
        
    # node 6, untuk cek genap/ganjil
    if n % 2 == 0:
        # node 7, hasilnya misal genap
        result.append("Genap")
    else:
        # node 8, hasilnya ganjil
        result.append("Ganjil")
        
    # node 9, untuk cek prima(tahap 1: kurang dari sama dengan 1)
    is_prime = True
    if n <= 1:
        # node 10
        is_prime = False
    else:
        # node 11, inisialisasi pembagi
        i = 2
        while i * i <= n:
            # node 12, cek sisa bagi
            if n % i == 0:
                # node 13, ditemukan pembagi, bukan prima -> langsung keluar loop
                is_prime = False
                break
            # node 14, increment pembagi
            i += 1
            
    # node 15, evaluasi hasil cek prima ato bukan
    if is_prime:
        # node 16
        result.append("Prima")
    else:
        # node 17
        result.append("Bukan Prima")
        
    # node 18, kembalikan hasil
    return result

# test cases
if __name__ == "__main__":
    print("n = 0  ->", analyze_number(0))
    print("n = -3 ->", analyze_number(-3))
    print("n = -2 ->", analyze_number(-2))
    print("n = 1  ->", analyze_number(1))
    print("n = 2  ->", analyze_number(2))
    print("n = 3  ->", analyze_number(3))
    print("n = 4  ->", analyze_number(4))
    print("n = 5  ->", analyze_number(5))
