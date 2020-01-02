list_moi = [];
def BaiTap7():
    for i in range (2000,3200):
        if i%7 == 0 and i%5 !=0:
            list_moi.append(i);
    return list_moi;


print(BaiTap7());

#Tinh giai thua

def TinhGiaiThua(n):
    if n == 1:
        return 1
    else:
        return n * TinhGiaiThua(n-1);

print("Vui long nhap so can tinh giai thu: ")
n=int(input())

print(TinhGiaiThua(n));


#Chuyen doi thuong sang hoa

class thuongsanghoa:
    chuoiso = "";

    def getString(self,sobatky):
        self.chuoiso = sobatky;

    def printString(self):
        print(self.chuoiso.upper());

i = thuongsanghoa();
print("Hay nhap 1 doan text chu thuong: ")
i.getString(input());
i.printString();

#

import math;
c=50;
h=30;
value = [];
print("Hay nhap chuoi s: ");
s = input();
items = s.split(',');
for d in items:
    value.append(str(int(round(math.sqrt((2*c*float(d)/h))))));
print(','.join(value));
