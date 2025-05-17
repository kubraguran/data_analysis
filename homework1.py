#1. Girilen sayının pozitif, negatif veya sıfır olduğunu yazan koşul

sayi = int(input("Bir sayı girin: "))

if sayi > 0:
    print("Pozitif")
elif sayi < 0:
    print("Negatif")
else:
    print("Sifir")

#2. Girilen sayının tek mi çift mi olduğunu yazan koşul

sayi = int(input("Bir sayi girin: "))

if sayi % 2 == 0:
    print("Çift")
else:
    print("Tek")

#3. Girilen nota göre harf aralığı
not_ = int(input("Notunuzu girin: "))

if 80 <= not_ <= 100:
    print("A")
elif 60 <= not_ < 80:
    print("B")
elif 40 <= not_ < 60:
    print("C")
else:
    print("D")


#4. İsim uzunluğu kontrolü
isim = input("İsminizi girin: ")

if len(isim) > 5:
    print("Uzun bir isminiz var.")
else:
    print("İsminiz:", isim)


#5. Girilen sayının asal olup olmadığını bulan kod (for ve while ile)

sayi = int(input("Sayi girin: "))

if sayi <= 1:
    print("Asal değil")
else:
    bolen_var_mi = False
    for i in range(2, sayi):
        if sayi % i == 0:
            bolen_var_mi = True
            break

    if bolen_var_mi:
        print("Asal değil")
    else:
        print("Asal")

#while ile
sayi = int(input("Sayi girin: "))

if sayi <= 1:
    print("Asal değil")
else:
    bolen_var_mi = False
    i = 2
    while i < sayi:
        if sayi % i == 0:
            bolen_var_mi = True
            break
        i += 1

    if bolen_var_mi:
        print("Asal değil")
    else:
        print("Asal")




#notlar = [45,85,75,50] içinde 75'in indisini bulma
notlar = [45, 85, 75, 50]

for i in range(len(notlar)):
    if notlar[i] == 75:
        print("75'in indeksi:", i)

#7. Girilen sayının faktöriyeli (for ve while)
sayi = int(input("Sayi girin: "))
faktoriyel = 1

for i in range(1, sayi + 1):
    faktoriyel *= i

print("Faktöriyel:", faktoriyel)

sayi = int(input("Sayi girin: "))
faktoriyel = 1
i = 1

while i <= sayi:
    faktoriyel *= i
    i += 1

print("Faktöriyel:", faktoriyel)


#8. Pozitif sayı girilene kadar isteyen for döngüsü

for _ in range(100):  # döngü sonsuz gibi çalışır
    sayi = int(input("Pozitif sayi girin: "))
    if sayi > 0:
        print("Teşekkürler! Pozitif sayi:", sayi)
        break


#9. Fonksiyon ile asal sayı kontrolü (for ve while)

def asal_mi(sayi):
    if sayi <= 1:
        return False
    for i in range(2, sayi):
        if sayi % i == 0:
            return False
    return True

sayi = int(input("Sayi girin: "))
print("Asal" if asal_mi(sayi) else "Asal değil")

def asal_mi(sayi):
    if sayi <= 1:
        return False
    i = 2
    while i < sayi:
        if sayi % i == 0:
            return False
        i += 1
    return True

sayi = int(input("Sayi girin: "))
print("Asal" if asal_mi(sayi) else "Asal değil")


