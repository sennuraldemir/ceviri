#Python: Bir Yazı İçerisindeki Türkçe Karakterleri İngilizce Karakterlere Çevirme İşlemi
önceki_karakterler =      ["ş",
                          "ç",
                          "ö",
                          "ğ",
                          "ü",
                          "ı",
                          "Ş",
                          "Ç",
                          "Ö",
                          "Ğ",
                          "Ü",
                          "İ"]

sonraki_karakterler =   ["s",
                         "c",
                         "o",
                         "g",
                         "u",
                         "i",
                         "S",
                         "C",
                         "O",
                         "G",
                         "U",
                         "I"]

metin = input("Çeviri yapılacak metni giriniz  :   ")
for i in range(12):
    metin=metin.replace(önceki_karakterler[i],sonraki_karakterler[i])
print(metin)

aranan_harf=input("Lütfen aradığınız harfi giriniz:\t")
adet=0
for karakter in metin:
    if karakter==aranan_harf:
        adet+=1
print(adet)


#Seymanur tarafından ekleme yapıldı....
def kontrol(str):
  sayac = 0
  for ch in str:
    if ch == 'ğ':
      sayac = sayac + 1
      return True
      break
    
metin=input('Metin : ')
if(kontrol(metin)==True):
      print('ğ karakteri metin içinde var')
else:
      print('ğ karakteri metin içinde yok')




