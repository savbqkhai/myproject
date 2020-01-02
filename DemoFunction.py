def congHaiSo(a,b):
    """Docstring
    """
    return a + b;

x = congHaiSo(1,2);
print("Ket qua la: ", x);
print(congHaiSo.__doc__);

#

list_so_nguyen_moi = [];
def chonloc(list_so_nguyen):
    for i in range (0,len(list_so_nguyen)):
        if list_so_nguyen[i]%2 == 0:
            list_so_nguyen_moi.append(list_so_nguyen[i]);
    return list_so_nguyen_moi;

list_so_nguyen = [1,2,3,6,3,9,20];

print(chonloc(list_so_nguyen))

#

list_so_moi = [];
list_so=[1,2,3,4,5,6,7,8,20];
chon_loc = lambda a : a%2 == 0;
list_so_moi = tuple(filter(chon_loc,list_so));
print(list_so_moi);

#
list_so_moi = [];
list_so=[1,2,3,4,5,6,7,8,20];
list_so_moi = tuple(filter(lambda a : a%2 == 0,list_so));
print(list_so_moi);

#

list_so_map = tuple(map(lambda a: a*3, list_so ));
print(list_so_map)
