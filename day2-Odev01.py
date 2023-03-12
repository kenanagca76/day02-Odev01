# Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.
ogrenciList=["Ali Sıfırıncı","Veli Birinci","Selami İkinci","Ayşe Ücüncü","Fatma Dördüncü","Hayriye Beşinci"]
print("**1**")
print(ogrenciList)

    
# Aldığı isim soy isim ile listeye öğrenci ekleyen
ogrenciList.append("Düriye Altıncı")
print("**2**")
print(ogrenciList)

# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
print("**3**")
ogrenciList.remove("Düriye Altıncı")
print(ogrenciList)

# Listeye birden fazla öğrenci eklemeyi mümkün kılan
ogrenciList.extend(["Düriye Altıncı","Cemile Yedinci"])
print("**4**")
print(ogrenciList)

# Listedeki tüm öğrencileri tek tek ekrana yazdıran
print("**5**")
for sinifim in ogrenciList:
    print(sinifim)

# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
print("**6**")
i=0
while i <len(ogrenciList):
    print( str(i) + " No'lu Ogrenci "+ ogrenciList[i])
    i+=1

# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
print("**7**")

for i in range(len(ogrenciList)-1, -1, -1):
    print(str(i) + " No'lu Ogrenci " + ogrenciList[i] + " listeden silindi.")
    del ogrenciList[i]
print("**8**")
print(ogrenciList)


