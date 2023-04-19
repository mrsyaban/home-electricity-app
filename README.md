# WireWorld
> Disusun untuk memenuhi Tugas 7 Implementasi Perancangan Perangkat Lunak IF2250 Rekayasa Perangkat Lunak.


## Deskripsi Singkat Program
Saat menggunakan perangkat listrik seringkali Miniatur Circuit Breaker (MCB) rumah “jeglek” dikarenakan perangkat listrik yang digunakan melebihi beban maksimal. namun, sulit untuk tahu sisa daya yang tersedia untuk dapat dipakai dan di ruangan mana yang masih tersedia daya yang cukup untuk perangkat yang ingin digunakan tersebut. dan juga banyak orang seringkali kaget saat melihat tagihan listrik rumah yang tiba-tiba melonjak dikarenakan jumlah tagihannya jauh diluar prediksinya. Oleh karena itu dibutuhkan aplikasi yang dapat menyimulasikan sistem kelistrikan rumah. lewat Wire Wolf, orang dapat mengetahui konsumsi daya dan status circuit breaker dan perangkat listrik  di rumahnya secara real time pada simulasi dan juga dapat memperkirakan konsumsi listrik per bulannya dengan akurat.
<br/>



## Requirement Program
* Python versi 3.7.6 atau lebih baru. Pastikan pula terdapat package PyPi (PIP) pada Python Anda.


## Cara Menjalankan Program
1. Pastikan sudah menyiapkan *environment* program serta komputer terhubung dengan internet.
2. Jalankan program `main.py` dengan menjalankan perintah `py src/main.py` pada *command prompt*.
3. Jika berhasil dijalankan, maka akan terdapat *window* Python pada komputer.

## Daftar Modul yang Diimplementasi
### 1. ElectricityManager

### 2. HouseManager

### 3. Simulation

### 4. RoomManager

### 5. ElectronicManager

## Daftar Tabel Basis Data
* Rumah
```
cid  name        type     notnull  dflt_value  pk
---  ----------  -------  -------  ----------  --
0    id          INTEGER  0                    1
1    nama        TEXT     1                    0
2    id_circuit  INTNOT   0                    0
```

* Ruangan
```
cid  name        type          notnull  dflt_value  pk
---  ----------  ------------  -------  ----------  --
0    id          INTEGER       0                    1
1    nama        VARCHAR(255)  1                    0
2    id_rumah    INT           1                    0
3    id_circuit  INT           1                    0
```

* Alat Listrik
```
cid  name              type          notnull  dflt_value  pk
---  ----------------  ------------  -------  ----------  --
0    id                INTEGER       0                    1
1    nama              TEXT          1                    0
2    ruangan_id        INT UNSIGNED  1                    0
3    daya              INT           1                    0
4    voltase           INT           1                    0
5    waktu_penggunaan  INT           1                    0
```

* Circuit Breaker
```
cid  name            type     notnull  dflt_value  pk
---  --------------  -------  -------  ----------  --
0    id              INTEGER  0                    1
1    kapasitas_daya  INT      1                    0
```



## Author
* [Mutawally Nawwar - 13521065]
* [Vieri Fajar Firdaus - 13521099]
* [Muhammad Rizky Sya’ban - 13521119]
* [Sulthan Dzaky Alfaro - 13521159]
* [Muhammad Habibi Husni - 13521169]
