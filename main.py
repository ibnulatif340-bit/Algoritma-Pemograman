# soal praktik gabungan aritmatika

# input

tugas = float(input("nilai tugas: "))
uts = float(input("nilai UTS: "))
uas = float(input("nilai UAS: "))
kehadiran = float(input("kehadiran (%): "))

# nilai akhir

nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)

# status

if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
    status = "LULUS DENGAN PREDIKAT"
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "LULUS"
else:
    status = "BELUM LULUS"

# output 
print("nilai akhir : ", nilai_akhir)
print("status :",status)
