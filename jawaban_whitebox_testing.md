# Laporan Tugas Whitebox Testing

## 1. Source Code Program
File source code telah dibuat dengan nama `number_analyzer.py`. Program ini dirancang untuk mendeteksi tiga sifat bilangan secara sekaligus:
- Positif, Negatif, atau Nol
- Genap atau Ganjil
- Prima atau Bukan Prima

Struktur kode memiliki `while loop` dan beberapa percabangan `if-else` bertingkat, menjadikannya cukup kompleks dan cocok untuk analisis pemahaman mendalam *Whitebox Testing*.

## 2. Gambaran Flow Graph
Berikut adalah *Flow Graph* dari program `number_analyzer.py` berdasarkan simpul (node) yang telah ditandai di dalam *source code*:

```mermaid
graph TD
    1{"1. if (n > 0)"}
    2["2. append('Positif')"]
    3{"3. elif (n < 0)"}
    4["4. append('Negatif')"]
    5["5. append('Nol')"]
    
    6{"6. if (n % 2 == 0)"}
    7["7. append('Genap')"]
    8["8. append('Ganjil')"]
    
    9{"9. if (n <= 1)"}
    10["10. is_prime = False"]
    
    11{"11. while (i * i <= n)"}
    12{"12. if (n % i == 0)"}
    13["13. is_prime = False (break)"]
    14["14. i += 1"]
    
    15{"15. if (is_prime)"}
    16["16. append('Prima')"]
    17["17. append('Bukan Prima')"]
    
    18(["18. Return Result"])

    %% Positif/Negatif/Nol
    1 -- True --> 2
    1 -- False --> 3
    2 --> 6
    3 -- True --> 4
    3 -- False --> 5
    4 --> 6
    5 --> 6
    
    %% Genap/Ganjil
    6 -- True --> 7
    6 -- False --> 8
    7 --> 9
    8 --> 9
    
    %% Prima Init
    9 -- True --> 10
    9 -- False --> 11
    10 --> 15
    
    %% While Loop Prima
    11 -- True --> 12
    11 -- False --> 15
    12 -- True --> 13
    12 -- False --> 14
    13 --> 15
    14 --> 11
    
    %% Cek Hasil Prima
    15 -- True --> 16
    15 -- False --> 17
    16 --> 18
    17 --> 18
```

## 3. Perhitungan Cyclomatic Complexity (CC)

Nilai Cyclomatic Complexity (V(G)) menentukan batas metrik maksimum *path independen* yang wajib diuji agar mencapai target pengujian *100% Branch Coverage*.

- **Metode 1: Berdasarkan Edge dan Node**
  Rumus: `V(G) = E - N + 2`
  - Jumlah Garis/Edge (E) = 24
  - Jumlah Simpul/Node (N) = 18
  - `V(G) = 24 - 18 + 2 = 8`

- **Metode 2: Berdasarkan Predicate Node (Simpul Keputusan)**
  Rumus: `V(G) = P + 1`
  - Jumlah *Predicate Node* / *Decision Node* (P) = 7 (yaitu Node 1, 3, 6, 9, 11, 12, dan 15)
  - `V(G) = 7 + 1 = 8`

Kesimpulan: **Cyclomatic Complexity program ini adalah 8.**

## 4. Independent Paths (Basis Paths) dan Test Cases

Berdasarkan nilai CC = 8, kita memiliki tepat **8 jalur eksekusi independen**. Setiap jalur ini bersifat independen karena minimum melewati satu ruas garis (*edge*) yang sebelumnya belum pernah dilewati oleh jalur lainnya. 

Berikut adalah penjabarannya beserta contoh input (*Test Case*) yang sudah tertuang pada program `number_analyzer.py`:

| Path | Jalur Node Eksekusi | Test Case | Keterangan Alur Program |
|------|---------------------|-----------|-------------------------|
| **1** | `1 -> 3 -> 5 -> 6 -> 7 -> 9 -> 10 -> 15 -> 17 -> 18` | `n = 0` | Nol, Genap, Bukan Prima |
| **2** | `1 -> 3 -> 4 -> 6 -> 8 -> 9 -> 10 -> 15 -> 17 -> 18` | `n = -3` | Negatif, Ganjil, Bukan Prima |
| **3** | `1 -> 3 -> 4 -> 6 -> 7 -> 9 -> 10 -> 15 -> 17 -> 18` | `n = -2` | Negatif, Genap, Bukan Prima |
| **4** | `1 -> 2 -> 6 -> 8 -> 9 -> 10 -> 15 -> 17 -> 18` | `n = 1` | Positif, Ganjil, Bukan Prima |
| **5** | `1 -> 2 -> 6 -> 7 -> 9 -> 11 -> 15 -> 16 -> 18` | `n = 2` | Positif, Genap, Prima (Loop Langsung Skip) |
| **6** | `1 -> 2 -> 6 -> 8 -> 9 -> 11 -> 15 -> 16 -> 18` | `n = 3` | Positif, Ganjil, Prima (Loop Langsung Skip) |
| **7** | `1 -> 2 -> 6 -> 7 -> 9 -> 11 -> 12 -> 13 -> 15 -> 17 -> 18` | `n = 4` | Positif, Genap, Bukan Prima (Masuk Loop, di-break) |
| **8** | `1 -> 2 -> 6 -> 8 -> 9 -> 11 -> 12 -> 14 -> 11 -> 15 -> 16 -> 18` | `n = 5` | Positif, Ganjil, Prima (Iterasi Loop Normal) |

Dengan membuat 8 test cases tersebut, Anda telah berhasil menyimulasikan *100% Path Coverage* untuk program Python ini.
