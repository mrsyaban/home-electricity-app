import sqlite3

conn = sqlite3.connect('db/wireWolf.db')
curr = conn.cursor()

curr.execute("""
CREATE TABLE circuit_breaker(
    id INTEGER PRIMARY KEY,
    kapasitas_daya INT NOT NULL
);
""")

curr.execute("""
CREATE TABLE rumah(
    id INTEGER PRIMARY KEY,
    nama TEXT NOT NULL,
    id_circuit INTNOT NULL, 
    FOREIGN KEY (id_circuit) REFERENCES circuit_breaker(id)
);
""")

curr.execute("""
CREATE TABLE ruangan (
    id INTEGER PRIMARY KEY,
    nama VARCHAR(255) NOT NULL,
    id_rumah INT NOT NULL,
    id_circuit INT NOT NULL,
    FOREIGN KEY (id_rumah) REFERENCES rumah(id),
    FOREIGN KEY (id_circuit) REFERENCES circuit_breaker(id)
);
""")

curr.execute("""

CREATE TABLE alat_listrik(
    id INTEGER PRIMARY KEY,
    nama TEXT NOT NULL,
    ruangan_id INT UNSIGNED NOT NULL,
    daya INT NOT NULL,
    voltase INT NOT NULL,
    waktu_penggunaan INT NOT NULL,
    FOREIGN KEY (ruangan_id) REFERENCES ruangan(id)
)
""")

conn.commit()
conn.close()
