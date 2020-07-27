# PLAYFAIR CIPHER
# JULIO ANDYAN JORDAN ARYANTO (24060117130078)
from array import *
from nltk import *


#fungsi untuk mengecek apakah ada huruf yang sama pada plain teks
#def equal, digunakan untuk menambahan huruf dummy pada 2 huruf yang sama
def Equal(teks, D):
    k = 0
    for i in range(len(teks)):
        if (i+1)< len(teks):
            if teks[i] == teks[i+1]:
                k = k + 1
                teks.insert(i+1, D)
    if k != 0 :
        print ("Terdapat beberapa karakter berurutan yang sama")
        print ("Sehingga Plainteks diubah menjadi: ")
    else :
        print ("Plainteks :")

    print (teks)
    print ("=============================")
    return teks


#inisialisasi
# kunci untuk tabel playfair adalah ATHEM
TPlayfair = [
    ["P", "R", "A", "C", "T"],
    ["I", "E", "M", "K", "S"],
    ["F", "B", "D", "G", "H"],
    ["L", "N", "O", "Q", "U"],
    ["V", "W", "X", "Y", "Z"]
]

# karakter dummy D
D = "X"

def begin():
    #List untuk hasil ekripsi
    TCipher = []
              
    #mulai


    #Relaisasi
    #-----Tahap 1 -----
    Pteks = input("masukan plain/cipher teks : ")
    #mengubah semua inputan teks menjadi kapital
    Pteks = Pteks.upper()
    #menghilangkan spasi di Pteks
    Ateks = []
    for j in range(len(Pteks)):
        if Pteks[j] != ' ' :
            if Pteks[j] == 'J':
                Ateks.append('I')
            else:
                Ateks.append(Pteks[j])
                
    print ("=============================")

    print ("Apa yang ingin Dilakukan ?")
    print ("1. Enkripsi")
    print ("2. Dekripsi")
    print ("=============================")

    pil = input("Masukan Pilihan Anda;")        
    #mengecek huruf berurutan yang sama
    if pil == '1':
        teks = Equal(Ateks, D)
    else :
        teks = Ateks

    #mengecek apakah Ateks Ganjil
    if len(teks) % 2 != 0:
        teks.insert(len(teks)+1, D)
    #-----End Tahap 1 -----
    
    #----- Tahap 2 -----
    #Operasi bigram
    teks = bigrams(teks)
    BList1= [] #ini hasil dari fungsi bigram python
    BList = [] # ini adalah bigram  yang akan digunakan
    for grams in teks:
        BList1.append(grams)

    #BList diisi disini
    for i in range(len(BList1)):
        if i == 0 :
            BList.append(BList1[i])
        else : #i!=0
            if i % 2 == 0:
                BList.append(BList1[i])
    #-----End Tahap 2-----

    #----- Tahap 3-----
    #Mulai operasi Playfair
    for i in range(len(BList)):
        #inisialisasi baris kolom
        b = []
        k = []
        for j in range(2):
            P = BList[i][j]
            #perhitungan untuk mendapatkan indeks dari
            #Plainteks P pada TPlayfair
            for s in range(5):
                for p in range(5):
                    if TPlayfair[s][p] == P :
                        b.append(s)
                        k.append(p)
        #enkripsi
        if pil == '1':
            #apabila dalam 1 kolom yang sama
            if k[0] == k[1] :
                b1 = b[0] + 1
                b2 = b[1] + 1
                if b1 == 5 :
                    b1 = 0
                if b2 == 5:
                    b2 =0
                k1 = k[0]
                k2 = k[1]
                
            #apabila dalam 1 baris yang sama
            elif b[0] == b[1] :
                b1 = b[0]
                b2 = b[1]
                k1 = k[0] + 1
                k2 = k[1] + 1
                if k1 == 5 :
                    k1 = 0
                if k2 == 5:
                    k2 =0
                
            #apabila posisi baris dan kolom beda
            else:
                k.reverse()
                b1 = b[0]
                b2 = b[1]
                k1 = k[0]
                k2 = k[1]
            #pada posisi ini sudah didapat index chiper
            #dari tabel Playfair
            #mulai mengambil nilai chipper dari TPlayfair
            #dan memasukan ke array TCipher
            TCipher.append(TPlayfair[b1][k1])
            TCipher.append(TPlayfair[b2][k2])
            
        #Dekripsi
        elif pil == '2':
            #apabila dalam 1 kolom yang sama
            if k[0] == k[1] :
                b1 = b[0] - 1
                b2 = b[1] - 1
                if b1 == -1 :
                    b1 = 4
                if b2 == -1:
                    b2 =4
                k1 = k[0]
                k2 = k[1]
                
            #apabila dalam 1 baris yang sama
            elif b[0] == b[1] :
                b1 = b[0]
                b2 = b[1]
                k1 = k[0] - 1
                k2 = k[1] - 1
                if k1 == -1 :
                    k1 = 4
                if k2 == -1:
                    k2 =4
                
            #apabila posisi baris dan kolom beda
            else:
                k.reverse()
                b1 = b[0]
                b2 = b[1]
                k1 = k[0]
                k2 = k[1]
            #pada posisi ini sudah didapat index chiper
            #dari tabel Playfair
            #mulai mengambil nilai chipper dari TPlayfair
            #dan memasukan ke array TCipher
            TCipher.append(TPlayfair[b1][k1])
            TCipher.append(TPlayfair[b2][k2])
        else :
            begin()
    if pil == '1':
        print ("Cipherteks yang didapatkan dari enkripsi Playfair adalah ="+"".join(TCipher))
        begin()
    elif pil == '2':
        print ("Plainteks yang didapatkan dari dekripsi Playfair adalah ="+" ".join(TCipher))
        begin()    
            
        
begin()        
        

        
