def chiahetcho5 (sonhiphan):
    sonhiphan = int(sonhiphan, 2)
    if sonhiphan % 5 == 0:
        return True
    else:
        return False
chuoisonhiphan = input("Nhap chuoi so nhi phan (phan tach boi dau phay): ")
sonhiphanlist = chuoisonhiphan.split(',')
sochiahetcho5 = [ so for so in sonhiphanlist if chiahetcho5 (so)]
if len(sochiahetcho5) > 0:
    ketqua = ','.join(sochiahetcho5)
    print("Cac so nhi phan chia het cho 5 la:",ketqua)
else:
    print("Khong co so nhi phan nao chia het cho 5 trong chuoi da nhap.")
