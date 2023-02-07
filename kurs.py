# SUPPORTED DEVICE ANDROID 6.1+ / IOs 7 / Win 7+
# CHANGE THIS FILE WITH CAREFULLY!!

#List Mata Uang Negara
List_Database = {
    '1. IDR' : 'Indonesia Rupiah',
    '2. MYR' : 'Ringgit Malaysia',
    '3. USD' : 'United States Dollar',
    '4. EUR' : 'Euro',
    '5. GBP' : 'British Pound Sterling',
    '6. SAR' : 'Saudi Riyal',
    '7. JPY' : 'Japanese Yen',
    '8. CNY' : 'Chinese Yuan',
    '9. KRW' : 'Korean WON',
}
print(List_Database)
#langkah kedua 

print("")

#membuat data uang semula
def rupiah():
    print("Aku ingin mengkonversi Uang")
    print(" 1. YA")
    print(" 2. OK")
    print(" 3. BAIK")
    
print("")

masukan=0
mata_uang=0
hasil=0

def konversikuy():
    print("Pilih mata uang yang dikonversi")
    print(" 1. IDR = Indonesian Rupiah (Rp.1)")
    print(" 2. MYR = Ringgit Malaysia (Rp. 3.534,41 )")
    print(" 3. USD = United States Dollar (Rp. 15.047,05)")
    print(" 4. EUR = Euro (Rp. 18.146,32)")
    print(" 5. GBP = British Pound Sterling (Rp.18238.37)")
    print(" 6. SAR = Saudi Riyal (Rp. 4.010,99)")
    print(" 7. JPY = Japanese Yen (Rp.114,33)")
    print(" 8. CNY = Chinese Yuan (Rp. 2.220,05)")
    print(" 9. KRW = Korean WON (Rp. 12,09")
    print(" 10. selesai")
    
print("")

masukan=0
mata_uang=0
hasil=0

rupiah()
pilihan=input("Masukkan Pilihan:")
pilihan=int(pilihan)
    
konversikuy()
pilihan=input("Masukkan Pilihan:")
pilihan=int(pilihan)
    
if pilihan==1 :
        masukan=input("Masukkan Nominal):")
        masukan=int(masukan)
        print("")
        mata_uang=1
        hasil=masukan*mata_uang
        print(f" {masukan} IDR senilai dengan {hasil} Rupiah")
        print("")
        
if pilihan==2 :
        masukan=input("Masukkan Nominal):")
        masukan=int(masukan)
        print("")
        mata_uang=3534
        hasil=masukan*mata_uang
        print(f" {masukan} MYR senilai dengan {hasil} Rupiah")
        print("")
        
if pilihan==3 :
        masukan=input("Masukkan Nominal):")
        masukan=int(masukan)
        print("")
        mata_uang=15047
        hasil=masukan*mata_uang
        print(f" {masukan} USD senilai dengan {hasil} Rupiah")
        print("")
        
if pilihan==4 :
        masukan=input("Masukkan Nominal):")
        masukan=int(masukan)
        print("")
        mata_uang=18146
        hasil=masukan*mata_uang
        print(f" {masukan} EUR senilai dengan {hasil} Rupiah")
        print("")
        
if pilihan==5 :
        masukan=input("Masukkan Nominal):")
        masukan=int(masukan)
        print("")
        mata_uang=18238
        hasil=masukan*mata_uang
        print(f" {masukan} GBP senilai dengan {hasil} Rupiah")
        print("")
        
if pilihan==6 :
        masukan=input("Masukkan Nominal):")
        masukan=int(masukan)
        print("")
        mata_uang=4010
        hasil=masukan*mata_uang
        print(f" {masukan} SAR senilai dengan {hasil} Rupiah")
        print("")
     
if pilihan==7 :
        masukan=input("Masukkan Nominal):")
        masukan=int(masukan)
        print("")
        mata_uang=114
        hasil=masukan*mata_uang
        print(f" {masukan} JPY senilai dengan {hasil} Rupiah")
        print("")
        
if pilihan==8 :
        masukan=input("Masukkan Nominal):")
        masukan=int(masukan)
        print("")
        mata_uang=2220
        hasil=masukan*mata_uang
        print(f" {masukan} CNY senilai dengan {hasil} Rupiah")
        print("")
        
if pilihan==9 :
        masukan=input("Masukkan Nominal):")
        masukan=int(masukan)
        print("")
        mata_uang=12
        hasil=masukan*mata_uang
        print(f" {masukan} KRW senilai dengan {hasil} Rupiah")
        print("")

#END
