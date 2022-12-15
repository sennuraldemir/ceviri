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



