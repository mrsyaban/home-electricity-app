<div align="center">
  <h1 align="center">Wire World</h1>

  <p align="center">
    A Home Electricity App
    <br />
  </p>
</div>
> Disusun untuk memenuhi Tugas 7 Implementasi Perancangan Perangkat Lunak IF2250 Rekayasa Perangkat Lunak.

![image](https://github.com/mrsyaban/home-electricity-app/assets/95738230/6bf0b400-22ad-4f53-83fa-a1772990efb4)

## Deskripsi Singkat Program
Pada perangkat lunak ini, terdapat berbagai fitur sehingga dapat menyelesaikan masalah pengguna. yang pertama adalah input yang menyesuaikan user. Input dalam perangkat lunak ini sangat menyesuaikan atau sangat dibebaskan kepada user. User dapat menginput perangkat-perangkat listrik maupun circuit breaker sesuai yang ada di rumahnya atau pun berkreasi sendiri. yang kedua adalah Simulasi ini bertujuan agar user mendapat gambaran sederhana dari rangkaian alat listrik yang telah diinputkan. Tidak hanya itu, dalam simulasi ini juga terdapat fitur status circuit breaker sebagai indikasi penggunaan daya yang berlebih. Yang terakhir adalha perkiraan konsumsi daya. Pada fitur ini, P/L menghitung perkiraan konsumsi daya bulanan berdasarkan lama waktu penggunaan harian dari semua perangkat listrik yang telah dimasukkan pengguna.

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
