import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, karakter, frekuensi):
        self.karakter = karakter
        self.frekuensi = frekuensi
        self.kiri = None
        self.kanan = None

    def __lt__(self, lain):
        return self.frekuensi < lain.frekuensi

def bangun_pohon_huffman(teks):
    frekuensi = Counter(teks)
    antrian_prioritas = [Node(karakter, frek) for karakter, frek in frekuensi.items()]
    heapq.heapify(antrian_prioritas)

    while len(antrian_prioritas) > 1:
        anak_kiri = heapq.heappop(antrian_prioritas)
        anak_kanan = heapq.heappop(antrian_prioritas)

        node_gabung = Node(None, anak_kiri.frekuensi + anak_kanan.frekuensi)
        node_gabung.kiri = anak_kiri
        node_gabung.kanan = anak_kanan

        heapq.heappush(antrian_prioritas, node_gabung)

    return antrian_prioritas[0]

def bangun_kode_huffman(akar):
    kode = {}

    def lintasi(node, kode_karakter):
        if node:
            if node.karakter is not None:
                kode[node.karakter] = kode_karakter
            lintasi(node.kiri, kode_karakter + "0")
            lintasi(node.kanan, kode_karakter + "1")

    lintasi(akar, "")
    return kode

def huffman_kompres(teks):
    akar = bangun_pohon_huffman(teks)
    kode = bangun_kode_huffman(akar)
    teks_terkompresi = ''.join(kode[karakter] for karakter in teks)
    return teks_terkompresi, kode

def huffman_dekompres(teks_terkompresi, kode):
    kode_terbalik = {kode_karakter: karakter for karakter, kode_karakter in kode.items()}
    teks_didekompresi = ""
    kode_buffer = ""
    for bit in teks_terkompresi:
        kode_buffer += bit
        if kode_buffer in kode_terbalik:
            teks_didekompresi += kode_terbalik[kode_buffer]
            kode_buffer = ""
    return teks_didekompresi

# Contoh penggunaan:
teks = "Ini adalah contoh teks"
teks_terkompresi, kode = huffman_kompres(teks)
print("Kompresi Teks:", teks_terkompresi)
print("Kode Huffman:", kode)

teks_didekompresi = huffman_dekompres(teks_terkompresi, kode)
print("Teks Didekompresi:", teks_didekompresi)
