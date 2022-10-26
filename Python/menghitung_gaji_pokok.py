mk = float(input("masukan masa kerja anda : "))
gapok = float(input("masukan gaji pokok anda : "))
if mk > 3:
    tjg = float(0.2*gapok)
else:
    tjg = float(0.1*gapok)
gatot = float(gapok + tjg)
print("gaji total anda adalah", gatot)