# PLAYFAIR CIPHER
# JULIO ANDYAN JORDAN ARYANTO (24060117130078)
# DIPONEGORO UNIVERSITY
# IT 17
from array import *
from nltk import *

# languages ind/eng
#fungsi untuk mengecek apakah ada huruf yang sama pada plain teks / function to check whether there are the same letters in plain text
#def equal, digunakan untuk menambahan huruf dummy pada 2 huruf yang sama / def equal, used to add dummy letters to the same 2 letters
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


#inisialisasi/ initiation
# kunci untuk tabel playfair adalah PRACTICE MAKES PERFECT / key :  PRACTICE MAKES PERFECT
TPlayfair = [
    ["P", "R", "A", "C", "T"],
    ["I", "E", "M", "K", "S"],
    ["F", "B", "D", "G", "H"],
    ["L", "N", "O", "Q", "U"],
    ["V", "W", "X", "Y", "Z"]
]

# dummy Dummy D
D = "X"

def begin():
    #List untuk hasil proses dekripsi dan enkripsi / list for decryption - encryption result
    TCipher = []
              
    #mulai/ start


    #Relaisasi/ realitation
    #-----Tahap 1 ----- / phase 1
    Pteks = input("masukan plain/cipher teks : ")
    #mengubah semua inputan teks menjadi kapital / capitalized the input
    Pteks = Pteks.upper()
    #menghilangkan spasi di Pteks / removing space from Pteks
    Ateks = []
    for j in range(len(Pteks)):
        if Pteks[j] != ' ' :
            if Pteks[j] == 'J':
                Ateks.append('I')
            else:
                Ateks.append(Pteks[j])
                
    print ("=============================")

    print ("Apa yang ingin Dilakukan ?")  #what you want to do ?
    print ("1. Enkripsi")
    print ("2. Dekripsi")
    print ("=============================")

    pil = input("Masukan Pilihan Anda;")    #input your choice    
    #mengecek huruf berurutan yang sama / check the same consecutive letters
    if pil == '1':
        teks = Equal(Ateks, D)
    else :
        teks = Ateks

    #mengecek apakah Ateks Ganjil / Check whether odd Ateks or not
    if len(teks) % 2 != 0:
        teks.insert(len(teks)+1, D)
    #-----End Tahap 1 ----- / end phase 1
    
    #----- Tahap 2 ----- / phase 2
    #Operasi bigram / bigrams operation
    teks = bigrams(teks)
    BList1= [] #ini hasil dari fungsi bigram python / list for bigram result
    BList = [] # ini adalah bigram  yang akan digunakan/ this is the bigram that will be used
    for grams in teks:
        BList1.append(grams)

    #BList diisi disini / inputing blist
    for i in range(len(BList1)):
        if i == 0 :
            BList.append(BList1[i])
        else : #i!=0
            if i % 2 == 0:
                BList.append(BList1[i])
    #-----End Tahap 2-----/ end phase 2

    #----- Tahap 3----- / phase 3
    #Mulai operasi Playfair/ begin playfair operation
    for i in range(len(BList)):
        #inisialisasi baris kolom/ initiate rows and columns
        b = []
        k = []
        for j in range(2):
            P = BList[i][j]
            #perhitungan untuk mendapatkan indeks dari 
            #Plainteks P pada TPlayfair / calculation to get the index of Plaintext P on TPlayfair
            for s in range(5):
                for p in range(5):
                    if TPlayfair[s][p] == P :
                        b.append(s)
                        k.append(p)
        #enkripsi / encryption
        if pil == '1':
            #apabila dalam 1 kolom yang sama / if in the same column
            if k[0] == k[1] :
                b1 = b[0] + 1
                b2 = b[1] + 1
                if b1 == 5 :
                    b1 = 0
                if b2 == 5:
                    b2 =0
                k1 = k[0]
                k2 = k[1]
                
            #apabila dalam 1 baris yang sama / if in the same row
            elif b[0] == b[1] :
                b1 = b[0]
                b2 = b[1]
                k1 = k[0] + 1
                k2 = k[1] + 1
                if k1 == 5 :
                    k1 = 0
                if k2 == 5:
                    k2 =0
                
            #apabila posisi baris dan kolom beda / if row and column positions are different
            else:
                k.reverse()
                b1 = b[0]
                b2 = b[1]
                k1 = k[0]
                k2 = k[1]
            #pada posisi ini sudah didapat index chiper dari tabel Playfair mulai mengambil nilai chipper dari TPlayfair dan memasukan ke array TCipher
            #right now the cipher index has been obtained from the Playfair table starting to take the chipper value from TPlayfair and insert it into the TCipher array
            TCipher.append(TPlayfair[b1][k1])
            TCipher.append(TPlayfair[b2][k2])
            
        #Dekripsi / Decryption
        elif pil == '2':
            #apabila dalam 1 kolom yang sama /  if in the same column
            if k[0] == k[1] :
                b1 = b[0] - 1
                b2 = b[1] - 1
                if b1 == -1 :
                    b1 = 4
                if b2 == -1:
                    b2 =4
                k1 = k[0]
                k2 = k[1]
                
            #apabila dalam 1 baris yang sama / if in the same row
            elif b[0] == b[1] :
                b1 = b[0]
                b2 = b[1]
                k1 = k[0] - 1
                k2 = k[1] - 1
                if k1 == -1 :
                    k1 = 4
                if k2 == -1:
                    k2 =4
                
            #apabila posisi baris dan kolom beda / if row and column positions are different
            else:
                k.reverse()
                b1 = b[0]
                b2 = b[1]
                k1 = k[0]
                k2 = k[1]
            #pada posisi ini sudah didapat index chiper dari tabel Playfair mulai mengambil nilai chipper dari TPlayfair dan memasukan ke array TCipher
            #right now the cipher index has been obtained from the Playfair table starting to take the chipper value from TPlayfair and insert it into the TCipher array
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
        

        
