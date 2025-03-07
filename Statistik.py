Nama="Serlia Turu Allo"
Nim="D0424312"
Tugas_Statistik="Contoh Soal Mean, Median,dan Modus"
print (Nama)
print (Nim)
print (Tugas_Statistik)

#N0. 1 Contoh Soal Mean
[100, 200, 159, 300, 250]
def hitung_mean(data):
    return sum(data) / len(data)

data_mean = [100, 200, 159, 300, 250]
mean = hitung_mean(data_mean)

print(f"Mean: {mean}")

#No.2 Contoh Soal Median 
[1200, 140, 160, 185, 200, 223, 240]
def hitung_median(data):
    data.sort()
    n = len(data)
    tengah = n // 2
    
    if n % 2 == 0:
        return (data[tengah - 1] + data[tengah]) / 2
    else:
        return data[tengah]

data_median = [1200, 140, 160, 185, 200, 223, 240]
median = hitung_median(data_median)

print(f"Median: {median}")

#No.3 Contoh Soal Modus 
[11, 21, 25, 31, 46, 40, 45, 55, 58]
def hitung_modus(data):
    frekuensi = {}
    
    for item in data:
        if item in frekuensi:
            frekuensi[item] += 1
        else:
            frekuensi[item] = 1
            
    modus = max(frekuensi, key=frekuensi.get)
    return modus

data_modus = [11, 21, 25, 31, 46, 40, 45, 55, 58]
modus = hitung_modus(data_modus)

print(f"Modus: {modus}")